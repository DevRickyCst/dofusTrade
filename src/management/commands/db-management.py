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


class Command(BaseCommand):
    help = "Fill Bdd with consumables"
    added_items_count = 0

    def add_arguments(self, parser):
        # nothing
        print()

    def handle(self, *args, **options):
        # Defining the host is optional and defaults to https://api.dofusdu.de
        configuration = dofusdude.Configuration(host="https://api.dofusdu.de")

        self.clean_db()

        self.call_right_api(configuration, ApiTypeEnum.CONSUMABLE)
        self.call_right_api(configuration, ApiTypeEnum.COSMETIC)
        self.call_right_api(configuration, ApiTypeEnum.RESOURCE)
        self.call_right_api(configuration, ApiTypeEnum.EQUIPMENT)

        print(
            "Added a Total of "
            + self.added_items_count.__str__()
            + " items to db"
        )

    #Call get_API_response() to retrieve all items according to api_type, for each item call insert_in_Item_Table()
    def call_right_api(self, configuration, api_type):
        added_items = 0
        try:
            api_response = self.get_API_response(
                configuration, api_type
            )
            print(
                "The response of " + api_type.name + " API contains "
                + len(api_response.items).__str__() + " "
                +  api_type.name
            )
            for item in api_response.items:
                self.insert_in_Item_Table(item, api_type)
                added_items += 1
            print(
                "Added " + added_items.__str__() + " " + api_type.name + " to db"
            )
        except Exception as e:
            print(
                "Exception when calling " + api_type.name + " API %s\n"
                 % e
            )

    # Delete every entries in the Item table
    def clean_db(self):
        all_bdd_Items = Item.objects.all()
        print("Found " + all_bdd_Items.count().__str__() + " entries in db")
        all_bdd_Items.delete()
        print("Deleted")

    # Create the api instance and return the response from the correct API
    def get_API_response(self, configuration, api_type):
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

    def insert_in_Item_Table(self, item, api_type):
        db_item = Item(
            ankama_id=item.ankama_id,
            name=item.name,
            type=item.type.name,
            level=item.level,
            image_urls=json.loads(item.image_urls.to_json()),
        )
        match api_type:
            case ApiTypeEnum.CONSUMABLE:
                db_item.categorie = "consumables"
            case ApiTypeEnum.EQUIPMENT:
                db_item.categorie = "equipments"
            case ApiTypeEnum.COSMETIC:
                db_item.categorie = "cosmetics"
            case ApiTypeEnum.RESOURCE:
                db_item.categorie = "resources"
        db_item.save()
        self.added_items_count += 1
