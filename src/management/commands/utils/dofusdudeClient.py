import dofusdude

from itemViewer.models import ItemCategory


class DofusdudeClient:

    def __init__(self) -> None:
        # Defining the host is optional and defaults to https://api.dofusdu.de
        self.configuration = dofusdude.Configuration(
            host="https://api.dofusdu.de"
        )
        self.solo_item_param = {
            "language": "fr",
            "game": "dofus2",
        }

        self.basic_params = self.solo_item_param.copy()
        self.basic_params.update(
            {
                "sort_level": "asc",
                "page_size": -1,
                "page_number": 1,
            }
        )

        self.full_params = self.basic_params.copy()
        self.full_params.update(
            {"filter_min_level": 0, "filter_max_level": 201}
        )

    def get_right_api_instance(self, api_type: ItemCategory):
        """Initialize dofusdude api from api_type"""
        with dofusdude.ApiClient(self.configuration) as api_client:
            if api_type == ItemCategory.EQUIPMENT:
                api_instance = dofusdude.EquipmentApi(api_client)
            elif api_type == ItemCategory.COSMETIC:
                api_instance = dofusdude.CosmeticsApi(api_client)
            elif api_type == ItemCategory.RESOURCE:
                api_instance = dofusdude.ResourcesApi(api_client)
            elif api_type == ItemCategory.CONSUMABLE:
                api_instance = dofusdude.ConsumablesApi(api_client)
            else:
                raise ValueError(f"{api_type} API not implemented yet")

        return api_instance

    def get_items_from_category(self, api_type: ItemCategory):
        """Retrieve all item from ItemCategory"""
        api_instance = self.get_right_api_instance(api_type)

        with dofusdude.ApiClient(self.configuration):
            if api_type == ItemCategory.EQUIPMENT:
                print(self.full_params)
                return api_instance.get_items_equipment_list(
                    **self.basic_params
                ).items
            elif api_type == ItemCategory.CONSUMABLE:
                return api_instance.get_items_consumables_list(
                    **self.basic_params
                ).items
            elif api_type == ItemCategory.COSMETIC:
                return api_instance.get_all_cosmetics_list(
                    **self.solo_item_param
                ).items
            elif api_type == ItemCategory.RESOURCE:
                return api_instance.get_all_items_resources_list(
                    **self.solo_item_param
                ).items

    def get_API_solo_response(self, api_type: ItemCategory, ankama_id):
        """Retrieve single item with ankama_id from ItemCategory"""
        api_instance = self.get_right_api_instance(api_type)

        params = self.solo_item_param.copy()
        params.update({"ankama_id": ankama_id})

        with dofusdude.ApiClient(self.configuration):
            if api_type == ItemCategory.EQUIPMENT:
                return api_instance.get_items_equipment_single(**params)
            elif api_type == ItemCategory.CONSUMABLE:
                return api_instance.get_items_consumables_single(**params)
            elif api_type == ItemCategory.COSMETIC:
                return api_instance.get_cosmetics_single(**params)
            elif api_type == ItemCategory.RESOURCE:
                return api_instance.get_items_resources_single(**params)

    def get_meta_elements(self):
        with dofusdude.ApiClient(self.configuration) as api_client:
            api_instance = dofusdude.MetaApi(api_client)
            return api_instance.get_meta_elements()
