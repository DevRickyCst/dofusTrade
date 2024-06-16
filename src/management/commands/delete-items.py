from django.core.management.base import BaseCommand

from itemViewer.models import (
    EffectSingle,
    Element,
    ImageUrls,
    Item,
    RecipeSingle,
)


class Command(BaseCommand):
    help = "Delete items related objects"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        print("Deleting Item ...")
        item_deleted = Item.objects.all().delete()
        print(f"Delete Items : {item_deleted}")

        # When too much item is deleted signals seems to not working
        if EffectSingle.objects.exists():
            print("Deleting EffectSingle ...")
            effectSingle_deleted = EffectSingle.objects.all().delete()
            print(f"Delete EffectSingle : {effectSingle_deleted}")

        if ImageUrls.objects.exists():
            print("Deleting ImageUrls ...")
            imageUrls_deleted = ImageUrls.objects.all().delete()
            print(f"Delete ImageUrls : {imageUrls_deleted}")

        if RecipeSingle.objects.exists():
            print("Deleting RecipeSingle ...")
            recipeSingle_deleted = RecipeSingle.objects.all().delete()
            print(f"Delete RecipeSingle : {recipeSingle_deleted}")

        if Element.objects.exists():
            print("Deleting Element ...")
            effect_deleted = Element.objects.all().delete()
            print(f"Delete Element : {effect_deleted}")
