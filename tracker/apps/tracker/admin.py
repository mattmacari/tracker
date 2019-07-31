from django.contrib import admin
from django.contrib.admin.decorators import register

from . import models


@admin.register(models.Weight)
class WeightAdmin(admin.ModelAdmin):
    fields = (
        "user",
        "measured_date",
        "weight",
        "scale_calc_body_fat",
        "scale_calc_lbm",
    )

    list_display = ("id", "user", "measured_date", "weight")

