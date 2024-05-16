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

# This class is a custom django-admin command, created to managebasic tasks on the database
# Calling it will clean every entry in in the Item Table and repopulate it using dofusdu.de api


class Command(BaseCommand):
    help = "Manage the database"
    added_items_count = 0

    def add_arguments(self, parser):
        # nothing
        print()

    def handle(self, *args, **options):
        self.clean_db()

        self.call_right_api(ApiTypeEnum.CONSUMABLE)
        self.call_right_api(ApiTypeEnum.COSMETIC)
        self.call_right_api(ApiTypeEnum.RESOURCE)
        self.call_right_api(ApiTypeEnum.EQUIPMENT)

        print(
            "Added a Total of "
            + self.added_items_count.__str__()
            + " items to db"
        )

    # Call get_API_response() to retrieve all items according to api_type, for each item call insert_in_Item_Table()
    def call_right_api(self, api_type):
        added_items = 0
        try:
            api_response = self.get_API_response(api_type)
            print(
                "The response of "
                + api_type.name
                + " API contains "
                + len(api_response.items).__str__()
                + " "
                + api_type.name
                + " items"
            )
            for item in api_response.items:
                self.insert_in_Item_Table(item, api_type)
                added_items += 1
            print(
                "Added "
                + added_items.__str__()
                + " "
                + api_type.name
                + " to db"
            )
        except Exception as e:
            print("Exception when calling " + api_type.name + " API %s\n" % e)

    # Delete every entries in the Item table
    def clean_db(self):
        all_bdd_Items = Item.objects.all()
        print("Found " + all_bdd_Items.count().__str__() + " entries in db")
        all_bdd_Items.delete()
        print("Deleted")

    # Create the api_instance and return the response from the correct API
    def get_API_response(self, api_type):
        # Defining the host is optional and defaults to https://api.dofusdu.de
        configuration = dofusdude.Configuration(host="https://api.dofusdu.de")
        with dofusdude.ApiClient(configuration) as api_client:
            # Common parameters to all API
            language = "fr"
            game = "dofus2"
            sort_level = "asc"
            page_size = -1
            page_number = 1

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
            if api_type == ApiTypeEnum.COSMETIC:
                api_instance = dofusdude.CosmeticsApi(api_client)
                return api_instance.get_all_cosmetics_list(
                    language,
                    game,
                    sort_level=sort_level,
                )
            if api_type == ApiTypeEnum.RESOURCE:
                api_instance = dofusdude.ResourcesApi(api_client)
                return api_instance.get_all_items_resources_list(
                    language,
                    game,
                    sort_level=sort_level,
                )

    # insert provided item in Item table, using api_type to fill categorie column
    def insert_in_Item_Table(self, item, api_type):
        db_item = Item(
            ankama_id=item.ankama_id,
            name=item.name,
            type=item.type.name,
            level=item.level,
            image_urls=json.loads(item.image_urls.to_json()),
            categorie=api_type.value,
        )
        db_item.save()
        self.added_items_count += 1
