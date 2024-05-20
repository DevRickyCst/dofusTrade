from django.db import models
from itemViewer.models import Item
from .character_models import Character

class SetCaracteristique(models.Model):
    """
    Represents a set of caracteristique.

    This model stores values about each caracteristique (vitalite, sagesse ...).
    """
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

    def __str__(self):
        return "id: " + self.id.__str__() 

class SetStuff(models.Model):
    """
    """
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
        return "id: " + self.id.__str__()

class Set(models.Model):
    character = models.ForeignKey(Character,on_delete= models.CASCADE)

    caracteristique = models.ForeignKey(SetCaracteristique, on_delete=models.CASCADE, null=True, blank=True)
    stuff = models.ForeignKey(SetStuff, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return ("id: " + self.id.__str__() + 
                "< characteristique_id: " + self.caracteristique.id.__str__() + 
                ", stuff_id: " + self.stuff.id.__str__() + " >")


