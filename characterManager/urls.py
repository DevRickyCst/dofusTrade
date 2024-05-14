from django.urls import path

from . import views

urlpatterns = [
    path("", views.view_personnages, name="index"),
    path("<int:id>", views.view_personnages, name="personnage")
]
