from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Workout(models.Model):

    STENGTH = "strength"
    CARDIO = "cardio"

    WORKOUT_TYPE_CHOICES = ((STENGTH, "Strength"), (CARDIO, "Cardio"))

    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

    DIFFICULTY_LEVELS = (
        (BEGINNER, "Beginner"),
        (INTERMEDIATE, "Intermediate"),
        (ADVANCED, "Advanced"),
    )

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete="cascade", db_index=True)
    type = models.CharField(
        max_length=250, choices=WORKOUT_TYPE_CHOICES, default=STENGTH, db_index=True
    )
    difficulty_level = models.CharField(
        max_length=250, choices=DIFFICULTY_LEVELS, default=BEGINNER, db_index=True
    )
    is_public = models.BooleanField(default=False)
    name = models.TextField()
    description = models.TextField(null=True, blank=True)

    tags = TaggableManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

