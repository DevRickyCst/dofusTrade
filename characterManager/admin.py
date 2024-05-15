from django.contrib import admin
from characterManager.models import Character, CharacterClass, CaracteristiqueSetClass


# Register your models here.
admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(CaracteristiqueSetClass)
