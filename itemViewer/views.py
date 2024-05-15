from src.custumRender import render
from itemViewer.dofusdudes import DofusDudeAPI
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

    # filter
    lvl_max = int(request.GET.get("lvl_max", 200))
    lvl_min = int(request.GET.get("lvl_min", 1))
    page_size = int(request.GET.get("page_size", 20))
    page_number = int(request.GET.get("page_number", 1))


    tab_var.update({
            'lvl_max' : lvl_max,
            'lvl_min' : lvl_min,
            'page_size' : page_size,
            'page_number' : page_number,
        })
    items = Item.objects.filter(
        categorie=item_type, level__lte=lvl_max, level__gte=lvl_min
    ).values()[page_size * (page_number - 1) : page_size * (page_number)]

    context.update(
        {
            "item_type": item_type,
            "items": items,
            "tab_var": tab_var,
        }
    )
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
    context.update(
        {
            #    'items': hello
        }
    )
    return render(request, "all_items.html", context=context)

def insert_resources(request):

    api = DofusDudeAPI("resources")
    data = api.get_all_item().items
    for item in data:
        correct_item = item.to_dict()
        correct_item.update({"categorie":'resources'})
        pk = correct_item.get('ankama_id')
        itemq, created = Item.objects.get_or_create(pk=pk, defaults=correct_item)
        # If the item already exists, update its fields with the new data
        if not created:
            for key, value in correct_item.items():
                setattr(itemq, key, value)
            itemq.save()
        try:
            itemq.save()
        except Exception as e:
            print(e)

    return render(request, "index.html", context=context)

def insert_equipments(request):

    api = DofusDudeAPI("equipments")
    data = api.get_all_item(maxx=1).items
    for item in data:
        print()
        correct_item = item.to_dict()
        correct_item.update({"categorie":'equipments'})
        pk = correct_item.get('ankama_id')
        itemq, created = Item.objects.get_or_create(pk=pk, defaults=correct_item)
        # If the item already exists, update its fields with the new data
        if not created:
            for key, value in correct_item.items():
                setattr(itemq, key, value)
            itemq.save()
        try:
            itemq.save()
        except Exception as e:
            print(e)

    return render(request, "index.html", context=context)

def insert_cosmetics(request):

    api = DofusDudeAPI("cosmetics")

    data = api.get_all_item().items
    for item in data:
        correct_item = item.to_dict()
        correct_item.update({"categorie":'cosmetics'})
        pk = correct_item.get('ankama_id')
        itemq, created = Item.objects.get_or_create(pk=pk, defaults=correct_item)
        # If the item already exists, update its fields with the new data
        if not created:
            for key, value in correct_item.items():
                setattr(itemq, key, value)
            itemq.save()
        try:
            itemq.save()
        except Exception as e:
            print(e)

    return render(request, "index.html", context=context)

def insert_consumables(request):

    api = DofusDudeAPI("consumables")
    for i in range(20):
        print(10+(i*10), 1+(i*10))
        data = api.get_item_list(lvl_max=(10+(i*10)), lvl_min=1+(i*10)).items
        for item in data:
            correct_item = item.to_dict()
            correct_item.update({"categorie":'consumables'})
            pk = correct_item.get('ankama_id')
            itemq, created = Item.objects.get_or_create(pk=pk, defaults=correct_item)
            # If the item already exists, update its fields with the new data
            if not created:
                for key, value in correct_item.items():
                    setattr(itemq, key, value)
                itemq.save()
            try:
                itemq.save()
            except Exception as e:
                print(e)

    return render(request, "index.html", context=context)