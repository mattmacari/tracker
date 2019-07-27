from django.contrib import admin
from django.contrib.admin.decorators import register

from . import models


@admin.register(models.Workout)
class WorkoutAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "name", "is_public", "type")