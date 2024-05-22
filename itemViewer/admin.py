from django.contrib import admin

from itemViewer.models import Item, ItemCategory, Itemtype, ImageUrls, Recipe,Effects 

# Register your models here.
admin.site.register(Item)
admin.site.register(Itemtype)
admin.site.register(ImageUrls)
admin.site.register(Recipe)
admin.site.register(Effects)
