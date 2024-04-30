import dofusdude

configuration = dofusdude.Configuration(host="https://api.dofusdu.de")


class DofusDudeAPI:

    def __init__(self, items_type: str) -> None:
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
        lvl_max: int = 200
    ):
        print(language, game, page_number, page_size, lvl_min, lvl_max)
        print("calling get item list")
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
        ankama_id,
        language: str = "fr",
        game: str = "dofus2",
    ):
        print("calling get item_single")
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
            elif self.items_type == "ressources":
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
