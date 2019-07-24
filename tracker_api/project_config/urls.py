from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("auth/", obtain_jwt_token),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/tracker/", include("apps.tracker.urls")),
    path("", views.index),
]
