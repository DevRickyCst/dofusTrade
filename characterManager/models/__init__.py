from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .character_models import Character, CharacterClass, Server
from .stuffs_models import Set, SetCaracteristique, SetStuff


@receiver(pre_save, sender=Set)
def set_default_values(sender, instance, **kwargs):
    if instance._state.adding:  # Check if the instance is new
        if not instance.caracteristique_id:
            instance.caracteristique = SetCaracteristique.objects.create()
        if not instance.stuff_id:
            instance.stuff = SetStuff.objects.create()


@receiver(post_save, sender=Character)
def create_related_sets(sender, instance, created, **kwargs):
    if created:
        set = Set.objects.create(character=instance)
        print(f"Created caracteristique: {set.id}")


@receiver(pre_save, sender=Character)
def set_default_values(sender, instance, **kwargs):
    if instance._state.adding:  # Check if the instance is new
        if not instance.server_id:
            instance.server = Server.objects.first()
        if not instance.character_class_id:
            instance.character_class = CharacterClass.objects.first()
