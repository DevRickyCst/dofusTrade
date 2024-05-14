import dofusdude

configuration = dofusdude.Configuration(host="https://api.dofusdu.de")


class DofusDudeAPI:
    """This class is mean to make dofusdude usage easier"""

    def __init__(self, items_type: str) -> None:
        """Init dofusdude api according to the string input"""
        self.items_type = items_type

        with dofusdude.ApiClient(configuration) as api_client:
            if self.items_type == "equipments":
                self.api = dofusdude.EquipmentApi(api_client)
            elif self.items_type == "cosmetics":
                self.api = dofusdude.CosmeticsApi(api_client)
            elif self.items_type == "resources":
                self.api = dofusdude.ResourcesApi(api_client)
            elif self.items_type == "consumables":
                self.api = dofusdude.ConsumablesApi(api_client)
            else:
                raise ValueError(f"{self.items_type} API not implemented yet")

    def get_item_list(
        self,
        language: str = "fr",
        game: str = "dofus2",
        page_number: int = 1,
        page_size: int = 20,
        lvl_min: int = 1,
        lvl_max: int = 200,
    ):
        """Get item list according to the __init__ api"""
        with dofusdude.ApiClient(configuration) as api_client:
            if self.items_type == "equipments":
                return self.api.get_items_equipment_list(
                    language,
                    game,
                    page_size=page_size,
                    page_number=page_number,
                    filter_min_level=lvl_min,
                    filter_max_level=lvl_max,
                )
            elif self.items_type == "cosmetics":
                return self.api.get_cosmetics_list(
                    language,
                    game,
                    page_size=page_size,
                    page_number=page_number,
                    filter_min_level=lvl_min,
                    filter_max_level=lvl_max,
                )
            elif self.items_type == "resources":
                return self.api.get_items_resources_list(
                    language,
                    game,
                    page_size=page_size,
                    page_number=page_number,
                    filter_min_level=lvl_min,
                    filter_max_level=lvl_max,
                )
            elif self.items_type == "consumables":
                return self.api.get_items_consumables_list(
                    language,
                    game,
                    page_size=page_size,
                    page_number=page_number,
                    filter_min_level=lvl_min,
                    filter_max_level=lvl_max,
                )
            else:
                raise ValueError(f"{self.items_type} API not implemented yet")

    def get_item_single(
        self,
        ankama_id: int,
        language: str = "fr",
        game: str = "dofus2",
    ):
        """Get single item according to the __init__ api"""
        with dofusdude.ApiClient(configuration) as api_client:
            if self.items_type == "equipments":
                return self.api.get_items_equipment_single(
                    language,
                    ankama_id,
                    game,
                )
            elif self.items_type == "cosmetics":
                return self.api.get_cosmetics_single(
                    language,
                    ankama_id,
                    game,
                )
            elif self.items_type == "resources":
                return self.api.get_items_resources_single(
                    language,
                    ankama_id,
                    game,
                )
            elif self.items_type == "consumables":
                return self.api.get_items_consumables_single(
                    language,
                    ankama_id,
                    game,
                )
            else:
                raise ValueError(f"{self.items_type} API not implemented yet")

    def get_all_item(
        self,
        language: str = "fr",
        game: str = "dofus2",
        minn=1,
        maxx=200,
    ):
        with dofusdude.ApiClient(configuration) as api_client:
            if self.items_type == "equipments":
                return self.api.get_all_items_equipment_list(
                    language,
                    game,
                    filter_min_level=minn,
                    filter_max_level=maxx,
                )
            elif self.items_type == "cosmetics":
                return self.api.get_all_cosmetics_list(
                    language,
                    game,
                    filter_min_level=minn,
                    filter_max_level=maxx,
                )
            elif self.items_type == "resources":
                return self.api.get_all_items_resources_list(
                    language,
                    game,
                    filter_min_level=minn,
                    filter_max_level=maxx,
                )
            elif self.items_type == "consumables":
                return self.api.get_all_items_consumables_list(
                    language,
                    game,
                    filter_min_level=minn,
                    filter_max_level=maxx,
                )
            else:
                raise ValueError(f"{self.items_type} API not implemented yet")
