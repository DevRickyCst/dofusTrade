from django.core.validators import MaxValueValidator, MinValueValidator
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


class Item(models.Model):
    ankama_id = models.IntegerField(primary_key=True, default=1)

    category = models.CharField(max_length=20, choices=ItemCategory.choices)
    type = models.ForeignKey(Itemtype, on_delete=models.CASCADE)

    # Global
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(200)]
    )
    pods = models.IntegerField(default=None, null=True)
    image_urls = models.ForeignKey(ImageUrls, on_delete=models.PROTECT)

    # Weapon
    ap_cost = models.IntegerField(default=None, null=True)
    range = models.IntegerField(default=None, null=True)
    max_cast_per_turn = models.IntegerField(default=None, null=True)
    is_weapon = models.BooleanField(default=False)
    is_two_handed = models.BooleanField(default=None, null=True)
    critical_hit_probability = models.IntegerField(default=None, null=True)
    critical_hit_bonus = models.IntegerField(default=None, null=True)

    # Conditionnal
    effects = models.ManyToManyField(Effects, default=None)
    recipe = models.ManyToManyField(Recipe, default=None)
    # conditions = models.JSONField(default=None, null=True)
    # parent_set = models.IntegerField(default=None, null=True)
    # condition_tree = models.IntegerField(default=None, null=True)

    def __str__(self):
        return "id: " + self.ankama_id.__str__() + ", name : " + self.name
