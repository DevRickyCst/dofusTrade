from django.db import models
from django.contrib.auth.models import User


class CharacterClass(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default="random")
    logo_url = models.CharField(max_length=100, default="random")

    def __str__(self) :
        return "id: " + self.id.__str__() + ", name : " + self.name


class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default="random")
    level = models.IntegerField(default=None)
    server = models.CharField(max_length=100)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to User model

    def __str__(self) :
        return "id: " + self.id.__str__() + ", name : " + self.name

