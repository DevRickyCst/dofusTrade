from django.urls import path

from . import views

urlpatterns = [
    path("", views.view_personnages, name="index"),
    path("<int:id>", views.view_personnages, name="personnage"),


    path("updateCaracSet", views.update_carac_set, name="updateCaracSet"),
    path("addCharacter", views.add_character, name="addCharacter"),
]
