from django.core.management.base import BaseCommand

from itemViewer.models import ItemCategory
from src.management.commands.__ApiTypeEnum import ApiTypeEnum as ApiTypeEnum

from .db_utils import clean_db, insert_item
from .dofusdudeClient import DofusdudeClient

# This class is a custom django-admin command, created to managebasic tasks on the database
# Calling it will clean every entry in in the Item Table and repopulate it using dofusdu.de api


class Command(BaseCommand):
    help = "Manage the database"
    added_items_count = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = DofusdudeClient()

    def add_arguments(self, parser):
        parser.add_argument(
            "--delete",
            action='store_true',
            help="Delete all item before inserting",
        )
        parser.add_argument(
            "--ankama-id", nargs="?", type=int, help="Add a single Ankama Id"
        )

        parser.add_argument(
            "--category",
            nargs="?",
            type=str,
            choices=["consumables", "equipments", "cosmetics", "resources"],
            help="Import only one category. Choices are: 'consumable', 'equipment', 'cosmetic', 'resource'",
        )

    def handle(self, *args, **options):

        if options["category"]:
            categories = [ItemCategory(options["category"])]
        else:
            categories = [
                ItemCategory.CONSUMABLE,
                ItemCategory.EQUIPMENT,
                ItemCategory.COSMETIC,
                ItemCategory.RESOURCE
            ]
        ankama_id = options.get("ankama_id", None)

        print(options["delete"])
        if options["delete"]:
            clean_db()
        exit()
        for category in categories:
            self.get_full_data_and_save(
                self.client.get_API_response(category),
                category,
            )

    def get_full_data_and_save(self, items, api_type):
        print(f'Start saving {api_type}')
        item_saved = 0
        item_failed = 0
        for item in items:
            try:
                insert_item(
                    self.client.get_API_solo_response(
                        api_type, item.ankama_id
                    ),
                    api_type,
                )
                item_saved += 1

            except Exception as e:
                item_failed += 1
                print(f"Fail to save item : { {item.ankama_id}, {item.name} }")
                print(e)
        print(f"Finish saving {api_type} :")
        print(f"Saved {item_saved} items.")
        print(f"Failed to save {item_failed} items.")
