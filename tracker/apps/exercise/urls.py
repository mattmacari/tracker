from django.urls import include, path

from . import views


urlpatterns = [
    path("workouts", view=views.ListWorkouts.as_view(), name="list_workouts"),
    path("workouts/create", view=views.CreateWorkout.as_view(), name="create_workout"),
    path("workouts/update/<int:pk>", view=views.UpdateWorkout.as_view(), name="update_workout"),
    path("workouts/delete/<int:pk>", view=views.DeleteWorkout.as_view(), name="delete_workout"),
    path("exercises", view=views.ExerciseListView.as_view(), name="list_exercises"),
    path("exercises/create", view=views.ExerciseCreateView.as_view(), name="create_exercise"),
    path("exercises/update/<int:pk>", view=views.ExerciseUpdateeView.as_view(), name="update_exercise"),
    path("exercises/delete/<int:pk>", view=views.ExerciseDeleteView.as_view(), name="delete_exercise"),
    path("", views.index, name="exercise_index"),
]

