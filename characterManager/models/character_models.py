from django.contrib.auth.models import User
from django.db import models

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
    server = models.ForeignKey(
        Server, on_delete=models.PROTECT, null=True, blank=True,
    )
    # Represents the Class of the character.
    character_class = models.ForeignKey(
        CharacterClass,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    # Represents the user who created the character.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Timestamp associated with the character.
    # created_at = models.DateTimeField(auto_now_add=True, null=True)
    # updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "id: " + self.id.__str__() + ", name : " + self.name

