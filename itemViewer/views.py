from django.shortcuts import render
from itemViewer.dofusdudes import DofusDudeAPI
from dofusdude.models.items_list_paged import ItemsListPaged
from django.urls import resolve

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
    '''Render HTML template 'all_items.html' with correct context'''
    # Use url to know the item type 
    item_type = resolve(request.path_info).url_name

    # Get tabs params from GET value
    if request.GET != {}:
        tab_var.update(request.GET)

    # TODO See how to better handle
    # Transform dict from request.GET to int
    for key, value in tab_var.items():
        if type(value) == list:
            tab_var[key] = int(value[0])

    # Init client
    api = DofusDudeAPI(item_type)
    data = api.get_item_list(**tab_var)
    listedItems = ItemsListPaged.from_dict(data)

    context = {
        'item_type': item_type,
        'items': listedItems.items,
        'tab_var': tab_var,
    }
    return render(request, "all_items.html", context=context)


def get_and_render_single_item(request, id):
    '''Render HTML template 'solo_item.html' with correct context'''
    # Use url to know the item type and add missing s
    item_type = f"{resolve(request.path_info).url_name}s"

    # Init client
    api = DofusDudeAPI(item_type)
    data = api.get_item_single(ankama_id=id)
    context = {
        'item_type': item_type,
        'item': data
    }    
    return render(request, "solo_item.html", context=context)