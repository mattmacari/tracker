from django.contrib import admin

from . import models

@admin.register(models.Workout)
class WorkoutAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "name", "is_public", "type")


@admin.register(models.ExerciseEquipment)
class ExerciseEquipmentModelAdmin(admin.ModelAdmin):

    list_display = ("id", "name")


@admin.register(models.Exercise)
class ExerciseModelAdmin(admin.ModelAdmin):

    list_display = ("id", "muscle", "name", "exercise_equipment")


@admin.register(models.MuscleGroup)
class MuscleGroupModelAdmin(admin.ModelAdmin):

    list_display = ("id", "muscle_name")


@admin.register(models.WorkoutExercise)
class WorkoutExerciseModelAdmin(admin.ModelAdmin):

    list_display = ("id", "workout", "exercise", "ordering")


@admin.register(models.WorkoutExerciseTarget)
class WorkoutExerciseTargetModelAdmin(admin.ModelAdmin):

    list_display = ("id", "workout_exercise", "set_number", "min_reps", "max_reps")


@admin.register(models.WorkoutPlan)
class WorkoutPlanModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.WorkoutPlanWorkout)
class WorkoutPlanWorkoutModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.UserWorkoutPlan)
class UserWorkoutPlanModelAdmin(admin.ModelAdmin):
    pass
