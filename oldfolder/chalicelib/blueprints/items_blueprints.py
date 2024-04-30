from chalice import Blueprint
from chalicelib.src.dofusdudes import DofusDudeAPI
from dofusdude.models.items_list_paged import ItemsListPaged
from chalicelib.utils.jinja2 import return_render_html_file

items_routes = Blueprint(__name__)

app_name = "item"

context = {"app": app_name}

def get_tabs_params(
    page_number: int=1,
    items_number: int=20,
    lvl_max: int=200,
    lvl_min: int=1,
):
    return {
        "page_number": int(page_number),
        "page_size": int(items_number),
        "lvl_max": int(lvl_max),
        "lvl_min": int(lvl_min),
    }

context = {"app": app_name}



@items_routes.route("/equipments", methods=["GET"])
@items_routes.route("equipments/id", methods=["GET"])
def return_equipments(id=None):
    item_type = "equipments"
    context["item_type"] = item_type
    api = DofusDudeAPI("equipments")
    # Initialization of dofusdude API Client
    if id is not None:
        data = api.get_item_single(ankama_id=int(id))
        context["item"] = data
    else:
        data = api.get_item_list()
        listedItems = ItemsListPaged.from_dict(data)
        context["items"] = listedItems.items
    return return_render_html_file(context)


@items_routes.route("/cosmetics", methods=["GET"])
@items_routes.route("cosmetics/id", methods=["GET"])
def return_cosmetics(id=None):
    item_type = "cosmetics"
    context["item_type"] = item_type
    # Initialization of dofusdude API Client
    api = DofusDudeAPI("cosmetics")

    if id is not None:
        data = api.get_item_single(ankama_id=int(id))
        context["item"] = data
    else:
        data = api.get_item_list()
        listedItems = ItemsListPaged.from_dict(data)
        context["items"] = listedItems.items
    return return_render_html_file(context)


@items_routes.route("/resources", methods=["GET"])
@items_routes.route("resources/id", methods=["GET"])
def return_equipments(id=None):
    item_type = "resources"

    context["item_type"] = item_type
    # Initialization of dofusdude API Client
    api = DofusDudeAPI("resources")

    if id is not None:
        data = api.get_item_single(ankama_id=int(id))
        context["item"] = data
    else:
        if items_routes.current_request.query_params is not None:
            context["tab_var"] = get_tabs_params(**items_routes.current_request.query_params)
            print(context["tab_var"])
        data = api.get_item_list(**context["tab_var"])
        listedItems = ItemsListPaged.from_dict(data)
        context["items"] = listedItems.items
    return return_render_html_file(context)


@items_routes.route("/consumables", methods=["GET"])
@items_routes.route("consumables/id", methods=["GET"])
def return_equipments(id=None):
    item_type = "consumables"
    context["item_type"] = item_type
    # Initialization of dofusdude API Client
    api = DofusDudeAPI("consumables")

    if id is not None:
        data = api.get_item_single(ankama_id=int(id))
        context["item"] = data
    else:
        data = api.get_item_list()
        listedItems = ItemsListPaged.from_dict(data)
        context["items"] = listedItems.items
    return return_render_html_file(context)
