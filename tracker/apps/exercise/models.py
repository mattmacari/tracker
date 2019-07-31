from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

from model_utils.choices import Choices
from model_utils.models import TimeStampedModel, StatusModel

DIFFICULTY_LEVELS = Choices(
    ("beginner", "Beginner"), ("intermediate", "Intermediate"), ("advanced", "Advanced")
)

TYPE_CHOICES = Choices(("strength", "Strength"), ("cardio", "Cardio"))

DAY_OF_WEEK_CHOICES = Choices(
    (1, 'Sunday'),
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Wednesday'),
    (5, 'Thursday'),
    (6, 'Friday'),
    (7, 'Saturday')

)


class WorkoutManager(models.Manager):
    def get_public_workouts(self) -> models.QuerySet:
        """"
        Returns all public workouts
        """
        return super().get_queryset().filter(is_public=True)

    def get_user_workouts(self, user: User) -> models.QuerySet:
        """
        Returns the provided user's workouts
        """
        return super().get_queryset().filter(user=user)


class Workout(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete="cascade", db_index=True)
    type = models.CharField(
        max_length=250,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES.strength,
        db_index=True,
    )
    difficulty_level = models.CharField(
        max_length=250,
        choices=DIFFICULTY_LEVELS,
        default=DIFFICULTY_LEVELS.beginner,
        db_index=True,
    )
    is_public = models.BooleanField(default=False)
    name = models.TextField()
    description = models.TextField(null=True, blank=True)

    tags = TaggableManager(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = WorkoutManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Workout'

class MuscleGroup(TimeStampedModel):

    BODY_PARTS = Choices(("upper", ("Upper")), ("lower", ("Lower")))

    id = models.BigAutoField(primary_key=True)

    muscle_name = models.TextField(null=False)
    body_part = models.CharField(
        max_length=50, choices=BODY_PARTS, default=BODY_PARTS.upper
    )

    def __str__(self):
        return self.muscle_name        

class ExerciseEquipment(TimeStampedModel):

    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Exercise(TimeStampedModel):

    id = models.BigAutoField(primary_key=True)

    muscle = models.ForeignKey(MuscleGroup, related_name="exercises", on_delete='cascade')
    exercise_equipment = models.ForeignKey(ExerciseEquipment, related_name="exercises", on_delete="cascade")
    difficulty_level = models.CharField(
        max_length=250,
        choices=DIFFICULTY_LEVELS,
        default=DIFFICULTY_LEVELS.beginner,
        db_index=True,
    )
    name = models.TextField(db_index=True)
    description = models.TextField(null=True, blank=True)
    video_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    tags = TaggableManager(blank=True)
    type = models.CharField(
        max_length=250,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES.strength,
        db_index=True,
    )

    def __str__(self):
        return self.name

class WorkoutExercise(TimeStampedModel):

    id = models.BigAutoField(primary_key=True)

    workout = models.ForeignKey(Workout, on_delete='cascade', related_name='workout_exercises')
    exercise = models.ForeignKey(Exercise, on_delete="cascade", related_name='workout_exercises')
    ordering = models.IntegerField()
    duration = models.DurationField(null=True)

    def __str__(self):
        return '{} - {}'.format(self.workout.name, self.exercise.name)

class WorkoutExerciseTarget(TimeStampedModel):

    id = models.BigAutoField(primary_key=True)

    workout_exercise = models.ForeignKey(WorkoutExercise, on_delete="cascade", related_name="targets")
    set_number = models.IntegerField()
    min_reps = models.IntegerField()
    max_reps = models.IntegerField()
    to_failure = models.BooleanField()
    rest_duration = models.IntegerField()

    def __str__(self):
        return '{} - {} set '.format(self.workout_exercise.workout.name, self.workout_exercise.exercise.name, self.set_number)


class WorkoutPlan(TimeStampedModel):

    id = models.BigAutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete='cascade', related_name='owned_workout_plans')
    is_public = models.BooleanField(default=False)
    name = models.TextField()
    summary = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    plan_duration = models.DurationField()
    difficulty_level = models.CharField(
        max_length=250,
        choices=DIFFICULTY_LEVELS,
        default=DIFFICULTY_LEVELS.beginner,
        db_index=True,
    )
    tags = TaggableManager(blank=True)

class WorkoutPlanWorkout(TimeStampedModel):

    id = models.BigAutoField(primary_key=True)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete='cascade', related_name='workouts')
    workout = models.ForeignKey(Workout, on_delete='cascade')
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES)


class UserWorkoutPlan(TimeStampedModel, StatusModel):

    STATUS = Choices('upcoming', 'inactive', 'current', 'past')

    id = models.BigAutoField(primary_key=True)
    assigned_user = models.ForeignKey(User, on_delete='cascade', related_name='assigned_workout_plans')
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete='cascade')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    notes = models.TextField()