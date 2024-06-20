from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

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


# Signal for validating chapeau type
@receiver(pre_save, sender=SetStuff)
def validate_chapeau_type(sender, instance, **kwargs):
    if instance.chapeau and instance.chapeau.type.name != "Chapeau":
        raise ValidationError("The selected item for chapeau is not of type 'chapeau'.")
    if instance.collier and instance.collier.type.name != "Amulette":
        raise ValidationError("The selected item for collier is not of type 'Amulette'.")
    if instance.anneau_1 and instance.anneau_1.type.name != "Anneau":
        raise ValidationError("The selected item for anneau_1 is not of type 'anneau_1'.")
    if instance.anneau_2 and instance.anneau_2.type.name != "Anneau":
        raise ValidationError("The selected item for anneau_2 is not of type 'anneau_2'.")
    if instance.ceinture and instance.ceinture.type.name != "Ceinture":
        raise ValidationError("The selected item for ceinture is not of type 'ceinture'.")
    if instance.botte and instance.botte.type.name != "Bottes":
        raise ValidationError("The selected item for botte is not of type 'botte'.")
    if instance.bouclier and instance.bouclier.type.name != "Bouclier":
        raise ValidationError("The selected item for bouclier is not of type 'bouclier'.")
    if instance.arme and not(instance.arme.is_weapon):
        print(instance.arme.is_weapon)
        raise ValidationError("The selected item for arme is not of type 'arme'.")