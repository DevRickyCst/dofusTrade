from django.shortcuts import render
from itemViewer.dofusdudes import DofusDudeAPI
from dofusdude.models.items_list_paged import ItemsListPaged
from django.urls import resolve
from itemViewer.models import Item

app_name = "item"

context = {"app": app_name}

tab_var = {
    "page_number": 1,
    "page_size": 20,
    "lvl_max": 200,
    "lvl_min": 1,
}


def index(request):
    return render(request, "index.html", context=context)


def get_and_render_all_items(request):
    """Render HTML template 'all_items.html' with correct context"""
    # Use url to know the item type
    item_type = resolve(request.path_info).url_name

    print()
    # filter
    lvl_max = int(request.GET.get("lvl_max", 200))
    lvl_min = int(request.GET.get("lvl_min", 1))
    page_size = int(request.GET.get("page_size", 20))
    page_number = int(request.GET.get("page_number", 1))

    print(request.GET)

    tab_var.update({
            'lvl_max' : lvl_max,
            'lvl_min' : lvl_min,
            'page_size' : page_size,
            'page_number' : page_number,
        })
    print(tab_var)
    items = Item.objects.filter(
        level__lte=lvl_max, level__gte=lvl_min
    ).values()[page_size * (page_number - 1) : page_size * (page_number)]

    context.update(
        {
            "item_type": item_type,
            "items": items,
            "tab_var": tab_var,
        }
    )
    print(context["tab_var"])
    return render(request, "all_items.html", context=context)


def get_and_render_single_item(request, id):
    """Render HTML template 'solo_item.html' with correct context"""
    # Use url to know the item type and add missing s
    item_type = f"{resolve(request.path_info).url_name}s"

    # Init client
    api = DofusDudeAPI(item_type)
    data = api.get_item_single(ankama_id=id)
    context.update({"item_type": item_type, "item": data})
    return render(request, "solo_item.html", context=context)


def test_item(request):

    hello = list(Item.objects.all().values())
    print(hello)
    context.update(
        {
            #    'items': hello
        }
    )
    return render(request, "all_items.html", context=context)
