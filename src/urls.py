from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("items/", include("itemViewer.urls")),
    path("", views.index, name="index"),
    path("personnages/", include("characterManager.urls")),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),    

]
