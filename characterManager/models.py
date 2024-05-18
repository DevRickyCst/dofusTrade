from django.contrib.auth.models import User
from django.db import models
from itemViewer.models import Item
from django.db.models.signals import post_save
from django.dispatch import receiver

class Server(models.Model):
    """
    Represents a single server class.

    This model stores information about a Server.
    """

    # Represents the name of the class.
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "id: " + self.id.__str__() + ", name : " + self.name


class CharacterClass(models.Model):
    """
    Represents a single character class.

    This model stores information about a class.
    """

    # Represents the name of the class.
    name = models.CharField(max_length=100, default="random", unique=True)
    # Represents the path to the class logo.
    logo_url = models.CharField(max_length=100, default="random")

    def __str__(self):
        return "id: " + self.id.__str__() + ", name : " + self.name
    
class Character(models.Model):
    """
    Represents a single character.

    This model stores information about each character.
    """

    # Represents the name of the character.
    name = models.CharField(max_length=100, null=False)
    # Represents the level of the character.
    level = models.IntegerField(default=200)
    # Represents the server of the character.
    default_server = Server.objects.first()
    server = models.ForeignKey(
        Server, on_delete=models.PROTECT, default=default_server
    )
    # Represents the Class of the character.
    default_character_class = CharacterClass.objects.first()
    character_class = models.ForeignKey(
        CharacterClass,
        on_delete=models.CASCADE,
        default=default_character_class,
    )
    # Represents the user who created the character.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Timestamp associated with the character.
    # created_at = models.DateTimeField(auto_now_add=True, null=True)
    # updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "id: " + self.id.__str__() + ", name : " + self.name


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

@receiver(post_save, sender=Character)
def create_caracteristique_set(sender, instance, created, **kwargs):
    if created:

        charac = CaracteristiqueSet.objects.create(
            user=instance.user, character=instance
        )
        print(f'Created caracteristique : {charac.id}')

        StuffSet.objects.create(
            user = instance.user, character = instance,
            caracteristique = charac
        )
