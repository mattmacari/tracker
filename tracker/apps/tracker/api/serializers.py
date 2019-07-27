from rest_framework import serializers
from django.contrib.auth.models import User

from .. import models


class WeightSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = models.Weight
        fields = [
            "id",
            "user",
            "measured_date",
            "weight",
            "scale_calc_body_fat",
            "scale_calc_lbm",
        ]
        depth = 1


# TODO: Refactor into generic


class UserSerializer(serializers.ModelSerializer):
    weight_set = WeightSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "weight_set"]

