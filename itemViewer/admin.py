from django.contrib import admin

from itemViewer.models import (
    EffectSingle,
    Element,
    ImageUrls,
    Item,
    Itemtype,
    Range,
    RecipeSingle,
)

# Register your models here.
admin.site.register(Item)
admin.site.register(Itemtype)
admin.site.register(ImageUrls)
admin.site.register(RecipeSingle)
admin.site.register(EffectSingle)
admin.site.register(Range)
admin.site.register(Element)
