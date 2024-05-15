from django.contrib import admin

from characterManager.models import (
    Character,
    CharacterClass,
    CaracteristiqueSetClass,
    Server,
)

# Register your models here.
admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(CaracteristiqueSetClass)
admin.site.register(Server)
