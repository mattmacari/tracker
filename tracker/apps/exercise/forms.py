from django import forms

from . import models


class WorkoutModelForm(forms.ModelForm):
    class Meta:
        model = models.Workout
        fields = [
            "type",
            "difficulty_level",
            "is_public",
            "name",
            "description",
            "tags",
        ]


class ExerciseModelForm(forms.ModelForm):
    class Meta:
        model = models.Exercise
        fields = [
            "muscle",
            "exercise_equipment",
            "difficulty_level",
            "name",
            "description",
            "video_url",
            "image_url",
            "type",
            "tags",
        ]


class WorkoutExerciseModelForm(forms.ModelForm):
    class Meta:
        model = models.WorkoutExercise
        fields = ["workout", "exercise", "ordering", "duration"]


class WorkoutExerciseTargetModelForm(forms.ModelForm):
    class Meta:
        model = models.WorkoutExerciseTarget
        fields = [
            "workout_exercise",
            "set_number",
            "min_reps",
            "max_reps",
            "to_failure",
            "rest_duration",
        ]


class WorkoutPlanModelForm(forms.ModelForm):
    class Meta:
        model = models.WorkoutPlan
        fields = [
            "is_public",
            "name",
            "summary",
            "description",
            "plan_duration",
            "difficulty_level",
            "tags",
        ]


class WorkoutPlanWorkoutModelForm(forms.ModelForm):
    class Meta:
        model = models.WorkoutPlanWorkout
        fields = ["workout_plan", "workout", "day_of_week"]


class UserWorkoutPlan(forms.ModelForm):
    class Meta:
        model = models.UserWorkoutPlan
        fields = ["assigned_user", "workout_plan", "start_date", "end_date", "notes"]

