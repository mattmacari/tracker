from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path("weights", views.ListWeights.as_view(), name="list_weight"),
    path("weights/create", views.CreateWeight.as_view(), name="create_weight"),
    path("weights/update/<int:pk>", views.UpdateWeight.as_view(), name="update_weight"),
    path("weights/delete/<int:pk>", views.DeleteWeight.as_view(), name="delete_weight"),
    path("", views.index, name="tracker_index"),
]

