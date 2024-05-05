from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("resources", views.get_and_render_all_items, name="resources"),
    path("consumables", views.get_and_render_all_items, name="consumables"),
    path("cosmetics", views.get_and_render_all_items, name="cosmetics"),
    path("equipments", views.get_and_render_all_items, name="equipments"),
    path(
        "resources/<int:id>", views.get_and_render_single_item, name="resource"
    ),
    path(
        "consumables/<int:id>",
        views.get_and_render_single_item,
        name="consumable",
    ),
    path(
        "cosmetics/<int:id>", views.get_and_render_single_item, name="cosmetic"
    ),
    path(
        "equipments/<int:id>",
        views.get_and_render_single_item,
        name="equipment",
    ),
    path("items/", views.test_item, name="items"),
]
