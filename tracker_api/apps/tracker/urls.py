from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("users", views.UserViewSet, basename="User")
router.register("weights", views.WeightViewSet, basename="Weight")

urlpatterns = [path("", include(router.urls))]

