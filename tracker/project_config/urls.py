from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("tracker/", include("apps.tracker.urls")),
    path("", views.index, name="home"),
]
