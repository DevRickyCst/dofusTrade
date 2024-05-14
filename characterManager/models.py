from django.db import models

class Character(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(max_length=100, default="random")
    level = models.IntegerField(default=None)
    server = models.CharField(max_length=100)
    character_class = models.CharField(max_length=100, default="iop")