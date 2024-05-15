from django.db import models
from django.contrib.auth.models import User

import json

class Server(models.Model):
    '''
    Represents a single server class.

    This model stores information about a Server.
    '''
    # Represents the name of the class.
    name = models.CharField(max_length=100, unique=True)
    def __str__(self) :
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

    def __str__(self) :
        return "id: " + self.id.__str__() + ", name : " + self.name


class Character(models.Model):
    """
    Represents a single character.

    This model stores information about each character.
    """
    # Represents the name of the character.
    name = models.CharField(max_length=100, default="random")
    # Represents the level of the character.
    level = models.IntegerField(default=None)
    # Represents the server of the character.
    server = models.ForeignKey(Server, on_delete=models.PROTECT, null=True)
    # Represents the Class of the character.
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    # Represents the user who created the character.
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # Timestamp associated with the character.
    #created_at = models.DateTimeField(auto_now_add=True, null=True)
    #updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self) :
        return "id: " + self.id.__str__() + ", name : " + self.name


class CaracteristiqueSetClass(models.Model):
    """
    Represents a set of caracteristique.

    This model stores values about each caracteristique (vitalite, sagesse ...).


    """
    # Represents the user who created the caracteristique set.
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
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


    def to_json(self):
        return json.dumps({
            'vitalite': self.vitalite,
            'agilite': self.agilite,
            'chance': self.chance,
            'force': self.force,
            'intelligence': self.intelligence,
            'sagesse': self.sagesse
        })