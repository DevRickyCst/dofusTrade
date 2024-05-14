from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("items/", include("itemViewer.urls")),
    path("log/", include("registration.urls")),
    path("", views.index, name="index"),
    path("personnages/", include("characterManager.urls")),

]
