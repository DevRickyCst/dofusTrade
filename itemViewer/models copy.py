from django.db import models

# Create your models here.
from django.db import models


class Itemtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return "id: " + self.id.__str__() + ", name : " + self.name


class Itemset(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    effects = models.JSONField(default=None, null=True)

    def __str__(self):
        return "id: " + self.id.__str__() + ", name : " + self.name


class Item(models.Model):
    ankama_id = models.IntegerField(primary_key=True, default=1)
    categorie = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=100, default="")
    type = models.ForeignKey(Itemtype, on_delete=models.CASCADE)
    level = models.IntegerField(default=None)
    image_urls = models.JSONField(default=None)
    description = models.CharField(max_length=1000, default=None, null=True)
    effects = models.JSONField(default=None, null=True)
    recipe = models.JSONField(default=None, null=True)
    conditions = models.JSONField(default=None, null=True)
    is_weapon = models.BooleanField(default=None, null=True)
    pods = models.IntegerField(default=None, null=True)
    parent_set = models.ForeignKey(Itemset, on_delete=models.CASCADE)
    critical_hit_probability = models.IntegerField(default=None, null=True)
    critical_hit_bonus = models.IntegerField(default=None, null=True)
    is_two_handed = models.BooleanField(default=None, null=True)
    max_cast_per_turn = models.IntegerField(default=None, null=True)
    ap_cost = models.IntegerField(default=None, null=True)
    range = models.IntegerField(default=None, null=True)
    condition_tree = models.IntegerField(default=None, null=True)
