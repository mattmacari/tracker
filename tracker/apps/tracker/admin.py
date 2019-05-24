from django.contrib import admin
from django.contrib.admin.decorators import register

from . import models


@admin.register(models.Weight)
class WeightAdmin(admin.ModelAdmin):
    pass