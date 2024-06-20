from django.urls import path

from . import views

urlpatterns = [
    path(
        "getitems",
        views.get_and_render_all_items_json,
        name="get_items",
    ),]
