from django.contrib import admin

from characterManager.models import (
    CaracteristiqueSet,
    Character,
    CharacterClass,
    Server,
    StuffSet,
)

# Register your models here.
admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(CaracteristiqueSet)
admin.site.register(Server)
admin.site.register(StuffSet)
