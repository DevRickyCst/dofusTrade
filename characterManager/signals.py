from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Character
from .models import CaracteristiqueSetClass

@receiver(post_save, sender=Character)
def create_caracteristique_set(sender, instance, created, **kwargs):
    if created:
        CaracteristiqueSetClass.objects.create(user=instance.user, character_id=instance)
