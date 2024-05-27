from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .items_meta import EffectSingle, ImageUrls, ItemCategory, Itemtype, RecipeSingle


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
    image_urls = models.OneToOneField(ImageUrls, on_delete=models.CASCADE)

    # Weapon
    ap_cost = models.IntegerField(default=None, null=True)
    range = models.IntegerField(default=None, null=True)
    max_cast_per_turn = models.IntegerField(default=None, null=True)
    is_weapon = models.BooleanField(default=False)
    is_two_handed = models.BooleanField(default=None, null=True)
    critical_hit_probability = models.IntegerField(default=None, null=True)
    critical_hit_bonus = models.IntegerField(default=None, null=True)

    # Conditionnal
    effects = models.ManyToManyField(EffectSingle, related_name="effects")
    recipe = models.ManyToManyField(RecipeSingle, related_name="recipes")
    # conditions = models.JSONField(default=None, null=True)
    # parent_set = models.IntegerField(default=None, null=True)
    # condition_tree = models.IntegerField(default=None, null=True)

    def __str__(self):
        return "id: " + self.ankama_id.__str__() + ", name : " + self.name
