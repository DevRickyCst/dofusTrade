import json
from datetime import date
from pprint import pprint

import dofusdude
import dofusdude.api_client
import requests
from django.core.management.base import BaseCommand, CommandError
from dofusdude.rest import ApiException

from itemViewer.models import Item
from src.management.commands.__ApiTypeEnum import ApiTypeEnum as ApiTypeEnum


# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
class Command(BaseCommand):
    help = "Fill Bdd with consumables"
    added_items_count = 0

    def add_arguments(self, parser):
        # nothing
        print()

    def handle(self, *args, **options):

        configuration = dofusdude.Configuration(host="https://api.dofusdu.de")

        self.clean_db()

        self.call_equipment_api(configuration)

        self.call_consumable_api(configuration)

    # Calls the consumables API, fetch all consumables and add them to bd with field categorie set as "consumable"
    def call_consumable_api(self, configuration):
        added_consumables = 0
        try:
            # Consumables endpoint
            json_api_response = self.get_API_response(
                configuration, ApiTypeEnum.CONSUMABLE
            ).to_json()
            json_consumable = json.loads(json_api_response)
            print(
                "The response of ConsumablesApi->get_items_consumables_list contains "
                + len(json_consumable["items"]).__str__()
                + " consumables\n"
            )
            for item in json_consumable["items"]:
                i = Item(
                    ankama_id=item["ankama_id"],
                    name=item["name"],
                    type=item["type"]["name"],
                    level=item["level"],
                    image_urls=item["image_urls"],
                )
                i.categorie = "consumables"
                i.save()
                self.added_items_count += 1
                added_consumables += 1
            print(
                "Added " + added_consumables.__str__() + " consumables to db"
            )
        except Exception as e:
            print(
                "Exception when calling ConsumablesApi->get_items_consumables_list: %s\n"
                % e
            )

    # Calls the consumables API, fetch all equipments and add them to bd with field categorie set as "equipment"
    def call_equipment_api(self, configuration):
        added_equipment = 0
        try:
            # List Equipment
            api_response = self.get_API_response(
                configuration, ApiTypeEnum.EQUIPMENT
            )
            print("The response of EquipmentApi->get_items_equipment_list:\n")
            # json_response = json.loads("{" + api_response.__str__() + "}")
            for item in api_response.items:
                # print(item.to_json())
                json_item = json.loads(item.to_json())
                i = Item(
                    ankama_id=json_item["ankama_id"],
                    name=json_item["name"],
                    type=json_item["type"]["name"],
                    level=json_item["level"],
                    image_urls=json_item["image_urls"],
                )
                i.categorie = "equipment"
                i.save()
                added_equipment += 1
            print(added_equipment)
            # print(json.dumps(json_response, indent=2))
        except Exception as e:
            print(
                "Exception when calling EquipmentApi->get_items_equipment_list: %s\n"
                % e
            )

    # Delete every entries in the Item table
    def clean_db(self):
        all_bdd_Items = Item.objects.all()
        deleted_items_count = 0
        print("Found " + all_bdd_Items.count().__str__() + " entries in db")
        if all_bdd_Items.count() != 0:
            for bdd_item in all_bdd_Items:
                bdd_item.delete()
                deleted_items_count += 1
        print("Deleted " + deleted_items_count.__str__() + " entries in db")

    # Create the api instance and return the response from the correct API
    def get_API_response(self, configuration, api_type):
        with dofusdude.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            language = "fr"  # str | a valid language code
            game = "dofus2"  # str |
            sort_level = "asc"  # str | sort the resulting list by level, default unsorted (optional)
            page_size = (
                -1
            )  # int | size of the results from the list. -1 disables pagination and gets all in one response. (optional)
            page_number = 1  # int | page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. (optional)

            if api_type == ApiTypeEnum.EQUIPMENT:
                api_instance = dofusdude.EquipmentApi(api_client)
                fields_item = [""]
                filter_min_level = 0
                filter_max_level = 201
                return api_instance.get_items_equipment_list(
                    language,
                    game,
                    page_size=page_size,
                    page_number=page_number,
                    sort_level=sort_level,
                    filter_min_level=filter_min_level,
                    filter_max_level=filter_max_level,
                    fields_item=fields_item,
                )
            if api_type == ApiTypeEnum.CONSUMABLE:
                api_instance = dofusdude.ConsumablesApi(api_client)
                return api_instance.get_items_consumables_list(
                    language,
                    game,
                    sort_level=sort_level,
                    page_size=page_size,
                    page_number=page_number,
                )

    """
# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
# Create an instance of the API class
api_instance = dofusdude.AlmanaxApi(api_client)
language = 'fr' # str | code
var_date = date.today() # date | yyyy-mm-dd

try:
    # Single Almanax Date
    api_response = api_instance.get_almanax_date(language, var_date)
    print("The response of AlmanaxApi->get_almanax_date:\n")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlmanaxApi->get_almanax_date: %s\n" % e)
"""


"""payload = {'page_size': '10', 'filter_max_level' : 2}
#r = requests.get('https://api.dofusdu.de/dofus2/fr/items/consumables/', params=payload)
r = requests.get('https://api.dofusdu.de/dofus2/fr/items/consumables?page-number=1&page-size=16')

print(r.status_code)
jsonResponse = json.loads(r.content)
jsonReadable = json.dumps(jsonResponse, indent=2)
print(len(jsonResponse["items"][0]))
print(jsonReadable)"""
