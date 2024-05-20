from .character_models import Character, Server, CharacterClass
from .stuffs_models import SetCaracteristique, SetStuff, Set
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


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
        charac = SetCaracteristique.objects.create(
            user=instance.user, character=instance
        )
        print(f'Created caracteristique: {charac.id}')

        stuffset = SetStuff.objects.create(
            user=instance.user, character=instance, caracteristique=charac
        )
        print(f'Created stuffset for character {stuffset.id}')

@receiver(pre_save, sender=Character)
def set_default_values(sender, instance, **kwargs):
    if instance._state.adding:  # Check if the instance is new
        if not instance.server_id:
            instance.server = Server.objects.first()
        if not instance.character_class_id:
            instance.character_class = CharacterClass.objects.first()