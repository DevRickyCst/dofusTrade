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
    path("insert_resources", views.insert_resources, name="insert_resources"),
    path(
        "insert_equipments", views.insert_equipments, name="insert_equipments"
    ),
    path("insert_cosmetics", views.insert_cosmetics, name="insert_cosmetics"),
    path(
        "insert_consumables",
        views.insert_consumables,
        name="insert_consumables",
    ),
]
