from django.shortcuts import render
from itemViewer.dofusdudes import DofusDudeAPI
from dofusdude.models.items_list_paged import ItemsListPaged
from django.urls import resolve

app_name = "item"


context = {"app": app_name}

tab_var = {
    "page_number": 1,
    "items_number": 20,
    "lvl_max": 200,
    "lvl_min": 1,          
}


def index(request):
    return render(request, "index.html", context=context)


def get_and_render_all_items(request):
    #Resolve view_name
    item_type = resolve(request.path_info).url_name

    #Get tabs params
    if request.GET != {}:
        tab_var.update(request.GET)



    api = DofusDudeAPI(item_type)
    data = api.get_item_list()
    listedItems = ItemsListPaged.from_dict(data)


    context = {
        'item_type': item_type,
        'items': listedItems.items,
        'tab_var': tab_var,
    }
    return render(request, "all_items.html", context=context)


def get_and_render_single_item(request, id):
    item_type = f"{resolve(request.path_info).url_name}s"
    api = DofusDudeAPI(item_type)
    data = api.get_item_single(ankama_id=id)
    print(data)
    context = {
        'item_type': item_type,
        'item': data
    }    
    return render(request, "solo_item.html", context=context)