from django.contrib.auth.models import User
from django.db import models
from itemViewer.models import Item
from .character_models import Character, Server, CharacterClass
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class CaracteristiqueSet(models.Model):
    """
    Represents a set of caracteristique.

    This model stores values about each caracteristique (vitalite, sagesse ...).


    """

    # Represents the user who created the caracteristique set.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Represents the user who created the caracteristique set.
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    # Value of vitalite
    vitalite = models.IntegerField(default=0)
    # Value of sagesse
    sagesse = models.IntegerField(default=0)
    # Value of agilite
    agilite = models.IntegerField(default=0)
    # Value of intelligence
    intelligence = models.IntegerField(default=0)
    # Value of chance
    chance = models.IntegerField(default=0)
    # Value of force
    force = models.IntegerField(default=0)


class StuffSet(models.Model):
    """
    """
    # Represents the user who created the caracteristique set.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Represents the user who created the caracteristique set.
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    # Represent the caracteristique set linked to the stuffset
    caracteristique = models.ForeignKey(CaracteristiqueSet, on_delete=models.CASCADE)
    ### STUFF
    chapeau = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name='stuffset_chapeau', blank=True)
    collier = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name='stuffset_collier', blank=True)
    anneau_1 = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name='stuffset_anneau_1', blank=True)
    anneau_2 = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name='stuffset_anneau_2', blank=True)
    ceinture = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name='stuffset_ceinture', blank=True)
    botte = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name='stuffset_botte', blank=True)
    bouclier = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name='stuffset_bouclier', blank=True)
    arme = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name='stuffset_arme', blank=True)

    def __str__(self):
        return "stuff_id: " + self.id.__str__() + f", user_id : {self.user.id}, caracteristique_id : {self.caracteristique.id}"

@receiver(pre_save, sender=Character)
def set_default_values(sender, instance, **kwargs):
    if instance._state.adding:  # Check if the instance is new
        if not instance.server_id:
            instance.server = Server.objects.first()
        if not instance.character_class_id:
            instance.character_class = CharacterClass.objects.first()

@receiver(post_save, sender=Character)
def create_related_sets(sender, instance, created, **kwargs):
    if created:
        charac = CaracteristiqueSet.objects.create(
            user=instance.user, character=instance
        )
        print(f'Created caracteristique: {charac.id}')

        stuffset = StuffSet.objects.create(
            user=instance.user, character=instance, caracteristique=charac
        )
        print(f'Created stuffset for character {instance.id}')