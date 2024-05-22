from django.db import models


class ItemCategory(models.TextChoices):
    CONSUMABLE = "consumables"
    EQUIPMENT = "equipments"
    COSMETIC = "cosmetics"
    RESOURCE = "resources"


class Itemtype(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return "id: " + self.id.__str__() + ", name : " + self.name


class ImageUrls(models.Model):
    icon = models.URLField(max_length=200)  # 60px*60px
    sd = models.URLField(max_length=200)  # 200px*200px
    hq = models.URLField(max_length=200)  # 400px*400px
    hd = models.URLField(max_length=200)  # 800px*800px

    def __str__(self):
        return "id: " + self.id.__str__()


class Recipe(models.Model):

    item_ankama_id = models.IntegerField()
    item_subtype = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return "id: " + self.id.__str__()


class Effects(models.Model):
    int_minimum = models.IntegerField(default=0)
    int_maximum = models.IntegerField(default=0)
    ignore_int_min = models.BooleanField(default=False)
    ignore_int_max = models.BooleanField(default=False)
    formatted = models.CharField(max_length=200)

    def __str__(self):
        return "id: " + self.id.__str__()
