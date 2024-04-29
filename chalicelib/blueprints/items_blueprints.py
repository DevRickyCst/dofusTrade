from chalice import Blueprint, Response
import dofusdude
from dofusdude.models.items_list_paged import ItemsListPaged
from chalicelib.utils.jinja2 import return_render_html_file


configuration = dofusdude.Configuration(host="https://api.dofusdu.de")

items_routes = Blueprint(__name__)

app_name = "item"

context = {"app": app_name}

game = 'dofus2'
language = "fr"

@items_routes.route("/equipments", methods=["GET"])
@items_routes.route("equipments/id", methods=["GET"])
def return_equipments(id=None):
    item_type = "equipments"
    context["item_type"] = item_type
    # Initialization of dofusdude API Client
    with dofusdude.ApiClient(configuration) as api_client:
        api_instance = dofusdude.EquipmentApi(api_client)
        if id is not None:
            data = api_instance.get_items_equipment_single(
                language=language, ankama_id=int(id), game=game
            )
            context["item"]= data
        else:
            data = api_instance.get_items_equipment_list(language, game)
            listedItems = ItemsListPaged.from_dict(data)
            context["items"]= listedItems.items
    return return_render_html_file(context)

@items_routes.route("/cosmetics", methods=["GET"])
@items_routes.route("cosmetics/id", methods=["GET"])
def return_cosmetics(id=None):
    item_type = "cosmetics"
    context["item_type"] = item_type
    # Initialization of dofusdude API Client
    with dofusdude.ApiClient(configuration) as api_client:
        api_instance = dofusdude.CosmeticsApi(api_client)
        if id is not None:
            data = api_instance.get_cosmetics_single(
                language=language, ankama_id=int(id), game=game
            )
            context["item"]= data
        else:
            data = api_instance.get_all_cosmetics_list(language, game)
            listedItems = ItemsListPaged.from_dict(data)
            context["items"]= listedItems.items
    return return_render_html_file(context)

@items_routes.route("/resources", methods=["GET"])
@items_routes.route("resources/id", methods=["GET"])
def return_equipments(id=None):
    item_type = "resources"
    context["item_type"] = item_type
    # Initialization of dofusdude API Client
    with dofusdude.ApiClient(configuration) as api_client:
        api_instance = dofusdude.ResourcesApi(api_client)
        if id is not None:
            data = api_instance.get_items_resources_single(
                language=language, ankama_id=int(id), game=game
            )
            context["item"]= data
        else:
            data = api_instance.get_items_resources_list(language, game)
            listedItems = ItemsListPaged.from_dict(data)
            context["items"]= listedItems.items
    return return_render_html_file(context)


@items_routes.route("/consumables", methods=["GET"])
@items_routes.route("consumables/id", methods=["GET"])
def return_equipments(id=None):
    item_type = "consumables"
    context["item_type"] = item_type
    # Initialization of dofusdude API Client
    with dofusdude.ApiClient(configuration) as api_client:
        api_instance = dofusdude.ConsumablesApi(api_client)
        if id is not None:
            data = api_instance.get_items_consumables_single(
                language=language, ankama_id=int(id), game=game
            )
            context["item"]= data
        else:
            data = api_instance.get_items_consumables_list(language, game)
            listedItems = ItemsListPaged.from_dict(data)
            context["items"]= listedItems.items
    return return_render_html_file(context)