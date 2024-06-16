from django.core.management.base import BaseCommand

from itemViewer.models import ItemCategory

from .utils.db_utils import insert_item
from .utils.dofusdudeClient import DofusdudeClient

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
            "--category",
            nargs="?",
            type=str,
            choices=["consumables", "equipments", "cosmetics", "resources"],
            help="Import only one category",
        )

    def handle(self, *args, **options):

        if options["category"]:
            categories = [ItemCategory(options["category"])]
        else:
            categories = [
                ItemCategory.CONSUMABLE,
                ItemCategory.EQUIPMENT,
                ItemCategory.COSMETIC,
                ItemCategory.RESOURCE,
            ]

        for category in categories:
            self.save_items(
                self.client.get_items_from_category(category),
                category,
            )

    def save_items(self, items, api_type):
        print(f"Start saving {api_type}")
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
                #print(f"Save item : {item.ankama_id}, {item.name} ")
                item_saved += 1

            except Exception as e:
                item_failed += 1
                print(f"Fail to save item :  {item.ankama_id}, {item.name}")
                print(e)
        print(f"Finish saving {api_type} :")
        print(f"Saved {item_saved} items.")
        print(f"Failed to save {item_failed} items.")
