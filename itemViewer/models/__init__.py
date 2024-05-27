from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

from .item import Item
from .items_meta import EffectSingle, ImageUrls, ItemCategory, Itemtype, RecipeSingle


@receiver(pre_delete, sender=Item)
def delete_associated_effects_and_recipes(sender, instance, **kwargs):

    # Supprimer les effets associés
    for effect in instance.effects.all():
        effect.delete()

    # Supprimer les recettes associées
    for recipe in instance.recipe.all():
        recipe.delete()


@receiver(post_delete, sender=Item)
def delete_associated_effects_and_recipes(sender, instance, **kwargs):
    if instance.image_urls:
        instance.image_urls.delete()
