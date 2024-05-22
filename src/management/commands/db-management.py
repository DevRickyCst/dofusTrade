import json
from datetime import date
from pprint import pprint

import dofusdude
import dofusdude.api_client
import requests
from django.core.management.base import BaseCommand, CommandError
from dofusdude.rest import ApiException

from itemViewer.models import Item, Itemtype, ImageUrls, Recipe, Effects, ItemCategory
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
        self.call_right_api(ItemCategory.EQUIPMENT)

        self.call_right_api(ItemCategory.CONSUMABLE)
        self.call_right_api(ItemCategory.COSMETIC)
        self.call_right_api(ItemCategory.RESOURCE)

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
                try:
                    full_item = self.get_API_solo_response(
                        ankama_id=item.ankama_id, api_type=api_type
                    )

                    item_type = full_item.type.to_dict()
                    item_type_instance, created = Itemtype.objects.get_or_create(id=item_type['id'],name=item_type['name'])
                    
                    image_Urls = full_item.image_urls.to_dict()
                    imageUrls = ImageUrls.objects.create(
                        icon = image_Urls['icon'],
                        sd = image_Urls['sd'],
                        hq = image_Urls['hq'],
                        hd = image_Urls['hd'],
                    )

                    list_recipe = []
                    if full_item.recipe != None:
                        for recip in full_item.recipe:
                            recipe = Recipe.objects.create(
                                item_ankama_id = recip.item_ankama_id,
                                item_subtype = recip.item_subtype,
                                quantity = recip.quantity
                            )
                            list_recipe.append(recipe)
                
                    list_effects = []
                    if full_item.effects != None:
                        for _effect in full_item.effects:
                            effect = Effects.objects.create(
                                int_minimum = _effect.int_minimum,
                                int_maximum = _effect.int_maximum,
                                ignore_int_min = _effect.ignore_int_min,
                                ignore_int_max = _effect.ignore_int_max,
                                formatted = _effect.formatted,
                            )
                            list_effects.append(effect)

                    items_params = {
                        'ankama_id': full_item.ankama_id,
                        'category': api_type,
                        'type': item_type_instance,
                        'name': full_item.name,
                        'description': full_item.description,
                        'level': full_item.level,
                        'pods': full_item.pods,
                        'image_urls': imageUrls,
                    }
                    if full_item.ap_cost:
                        items_params['ap_cost'] = full_item.ap_cost
                    #if full_item.range:
                    #    items_params['range'] = full_item.range
                    if full_item.max_cast_per_turn:
                        items_params['max_cast_per_turn'] = full_item.max_cast_per_turn
                    if full_item.is_weapon:
                        items_params['is_weapon'] = full_item.is_weapon
                    if full_item.is_two_handed:
                        items_params['is_two_handed'] = full_item.is_two_handed
                    if full_item.critical_hit_probability:
                        items_params['critical_hit_probability'] = full_item.critical_hit_probability
                    if full_item.critical_hit_bonus:
                        items_params['critical_hit_bonus'] = full_item.critical_hit_bonus

                    item = Item.objects.create(**items_params)

                    for effecst in list_effects:
                        item.effects.add(effecst)
                    for rcsp in list_recipe:
                        item.recipe.add(rcsp)

                    added_items += 1
                except Exception as e:
                    print(f'API BY id fail for ankama_id {item.ankama_id} excep as {e}')
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

            if api_type == ItemCategory.EQUIPMENT:
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
            if api_type == ItemCategory.CONSUMABLE:
                api_instance = dofusdude.ConsumablesApi(api_client)
                return api_instance.get_items_consumables_list(
                    language,
                    game,
                    sort_level=sort_level,
                    page_size=page_size,
                    page_number=page_number,
                )
            if api_type == ItemCategory.COSMETIC:
                api_instance = dofusdude.CosmeticsApi(api_client)
                return api_instance.get_all_cosmetics_list(
                    language,
                    game,
                    sort_level=sort_level,
                )
            if api_type == ItemCategory.RESOURCE:
                api_instance = dofusdude.ResourcesApi(api_client)
                return api_instance.get_all_items_resources_list(
                    language,
                    game,
                    sort_level=sort_level,
                )

    def get_API_solo_response(self, api_type, ankama_id):
        # Defining the host is optional and defaults to https://api.dofusdu.de
        configuration = dofusdude.Configuration(host="https://api.dofusdu.de")
        with dofusdude.ApiClient(configuration) as api_client:
            # Common parameters to all API
            language = "fr"
            game = "dofus2"

            if api_type == ItemCategory.EQUIPMENT:
                api_instance = dofusdude.EquipmentApi(api_client)
                return api_instance.get_items_equipment_single(
                    language,
                    ankama_id,
                    game,
                )
            if api_type == ItemCategory.CONSUMABLE:
                api_instance = dofusdude.ConsumablesApi(api_client)
                return api_instance.get_items_consumables_single(
                    language,
                    ankama_id,
                    game,
                )
            if api_type == ItemCategory.COSMETIC:
                api_instance = dofusdude.CosmeticsApi(api_client)
                return api_instance.get_cosmetics_single(
                    language,
                    ankama_id,
                    game,
                )
            if api_type == ItemCategory.RESOURCE:
                api_instance = dofusdude.ResourcesApi(api_client)
                return api_instance.get_items_resources_single(
                    language,
                    ankama_id,
                    game,
                )
