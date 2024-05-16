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

        self.call_consumable_api(configuration)

        self.call_equipment_api(configuration)

        self.call_cosmetic_api(configuration)
        
        self.call_resource_api(configuration)

        print(
            "Added a Total of "
            + self.added_items_count.__str__()
            + " items to db"
        )

    # Calls the consumables API, fetch all consumables and add them to bd with field categorie set as "consumable"
    def call_consumable_api(self, configuration):
        added_consumables = 0
        api_type = ApiTypeEnum.CONSUMABLE
        try:
            json_api_response = self.get_API_response(
                configuration, api_type
            ).to_json()
            json_consumable = json.loads(json_api_response)
            print(
                "The response of ConsumablesApi->get_items_consumables_list contains "
                + len(json_consumable["items"]).__str__()
                + " consumables"
            )
            for item in json_consumable["items"]:
                self.insert_in_Item_Table(item, api_type)
                added_consumables += 1
            print(
                "Added " + added_consumables.__str__() + " consumables to db"
            )
        except Exception as e:
            print(
                "Exception when calling ConsumablesApi->get_items_consumables_list: %s\n"
                % e
            )

    # Calls the equipment API, fetch all equipments and add them to bd with field categorie set as "equipment"
    def call_equipment_api(self, configuration):
        added_equipment = 0
        api_type = ApiTypeEnum.EQUIPMENT
        try:
            api_response = self.get_API_response(
                configuration, api_type
            )
            print(
                "The response of EquipmentApi->get_items_equipment_list contains "
                + len(api_response.items).__str__()
                + " equipments"
            )
            for item in api_response.items:
                json_item = json.loads(item.to_json())
                self.insert_in_Item_Table(json_item, api_type)
                added_equipment += 1
            print(added_equipment)
        except Exception as e:
            print(
                "Exception when calling EquipmentApi->get_items_equipment_list: %s\n"
                % e
            )

    def call_cosmetic_api(self, configuration):
        added_cosmetic = 0
        api_type = ApiTypeEnum.COSMETIC
        try:
            api_response = self.get_API_response(
                configuration, api_type
            )
            print(
                "The response of CosmeticApi->get_all_cosmetics_list contains "
                + len(api_response.items).__str__()
                + " cosmetics"
            )
            for item in api_response.items:
                json_item = json.loads(item.to_json())
                self.insert_in_Item_Table(json_item, api_type)
                added_cosmetic += 1
            print(added_cosmetic)
        except Exception as e:
            print(
                "Exception when calling CosmeticApi->get_all_cosmetics_list: %s\n"
                % e
            )

    def call_resource_api(self, configuration):
        added_resource = 0
        api_type = ApiTypeEnum.RESOURCE
        try:
            api_response = self.get_API_response(
                configuration, api_type
            )
            print(
                "The response of ResourcesApi->get_all_items_resources_list contains "
                + len(api_response.items).__str__()
                + " resources"
            )
            for item in api_response.items:
                json_item = json.loads(item.to_json())
                self.insert_in_Item_Table(json_item, api_type)
                added_resource += 1
            print(added_resource)
        except Exception as e:
            print(
                "Exception when calling ResourcesApi->get_all_items_resources_list: %s\n"
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


    def insert_in_Item_Table(self, json_item, api_type):
        item = Item(
            ankama_id=json_item["ankama_id"],
            name=json_item["name"],
            type=json_item["type"]["name"],
            level=json_item["level"],
            image_urls=json_item["image_urls"],
        )
        match api_type:
            case ApiTypeEnum.CONSUMABLE:
                item.categorie = "consumables"
            case ApiTypeEnum.EQUIPMENT:
                item.categorie = "equipments"
            case ApiTypeEnum.COSMETIC:
                item.categorie = "cosmetics"
            case ApiTypeEnum.RESOURCE:
                item.categorie = "resources"
        item.save()
        self.added_items_count += 1
