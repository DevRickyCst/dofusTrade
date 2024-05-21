from django.urls import resolve

from itemViewer.dofusdudes import DofusDudeAPI
from itemViewer.models import Item
from src.custumRender import render

app_name = "items"

context = {"app": app_name}

tab_var = {
    "page_number": 1,
    "page_size": 20,
    "lvl_max": 200,
    "lvl_min": 1,
}


def index(request):
    return render(request, context=context)


def get_and_render_all_items(request):
    """Render HTML template 'all_items.html' with correct context"""
    # Use url to know the item type
    item_type = resolve(request.path_info).url_name

    # filter
    lvl_max = int(request.GET.get("lvl_max", 200))
    lvl_min = int(request.GET.get("lvl_min", 1))
    page_size = int(request.GET.get("page_size", 20))
    page_number = int(request.GET.get("page_number", 1))

    tab_var.update(
        {
            "lvl_max": lvl_max,
            "lvl_min": lvl_min,
            "page_size": page_size,
            "page_number": page_number,
        }
    )
    items = Item.objects.filter(
        categorie=item_type, level__lte=lvl_max, level__gte=lvl_min
    ).values()[page_size * (page_number - 1) : page_size * (page_number)]

    context.update(
        {
            "display_style": "all_items",
            "item_type": item_type,
            "items": items,
            "tab_var": tab_var,
        }
    )
    print(context)
    return render(request, context=context)


def get_and_render_single_item(request, id):
    """Render HTML template 'solo_item.html' with correct context"""
    # Use url to know the item type and add missing s
    item_type = f"{resolve(request.path_info).url_name}s"
    # Init client
    api = DofusDudeAPI(item_type)
    data = api.get_item_single(ankama_id=id)
    context.update(
        {"display_style": "solo_item", "item_type": item_type, "item": data}
    )
    return render(request, context=context)
