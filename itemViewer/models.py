from django.db import models

# Create your models here.
from django.db import models
 
class item(models.Model):
    id = models.IntegerField(primary_key=True),
    categorie = models.CharField(max_length=20),
    name = models.CharField(max_length=100),
    type = models.CharField(max_length=30),
    level = models.IntegerField(),
    image_icon = models.CharField(max_length=100),
    image_sd = models.CharField(max_length=100),
    image_hq = models.CharField(max_length=100),
    image_hd = models.CharField(max_length=100),
    description = models.CharField(max_length=1000),
    effects = models.JSONField(),
    recipe = models.JSONField(),
    condition_tree = models.JSONField(),
