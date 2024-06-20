from django.urls import path

from . import views

urlpatterns = [
    path("updateCaracSet", views.update_carac_set, name="updateCaracSet"),
    path("addCharacter", views.add_character, name="addCharacter"),
    path("deleteCharacter", views.delete_character, name="deleteCharacter"),
]
