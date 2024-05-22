from django.contrib import admin

from characterManager.models import (
    Character,
    CharacterClass,
    Server,
    Set,
    SetCaracteristique,
    SetStuff,
)

# Register your models here.
admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(SetStuff)
admin.site.register(Server)
admin.site.register(SetCaracteristique)
admin.site.register(Set)
