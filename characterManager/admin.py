from django.contrib import admin

from characterManager.models import (
    Character,
    CharacterClass,
    Server,
    SetCaracteristique,
    SetStuff,
    Set,
)

# Register your models here.
admin.site.register(Character)
admin.site.register(CharacterClass)
admin.site.register(SetStuff)
admin.site.register(Server)
admin.site.register(SetCaracteristique)
admin.site.register(Set)
