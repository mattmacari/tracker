from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .. import models


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This provides functionality to list and detial the User information
    """

    permission_classes = (IsAuthenticated,)

    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


# #######################################
# Weight Tracking Views
# #######################################


class WeightViewSet(viewsets.ModelViewSet):
    """
    Viewset for the `Weight` model.
    """

    permission_classes = (IsAuthenticated,)

    model = models.Weight
    # queryset = models.Weight.objects.all()
    serializer_class = serializers.WeightSerializer

    def get_queryset(self):
        user = self.request.user
        return models.Weight.objects.filter(user=user)
