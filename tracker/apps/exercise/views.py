from django.shortcuts import render
from django.urls import reverse_lazy

from vanilla.model_views import ListView, CreateView, UpdateView, DeleteView

from . import models
from . import forms



def index(request):
    return render(request, "exercise/index.html")

# ########################################
# Workouts
# ########################################
 
class ListWorkouts(ListView):
    model = models.Workout

    def get_queryset(self):
        return self.model.objects.get_public_workouts().order_by('name')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['user_workouts'] = self.model.objects.get_user_workouts(self.request.user).order_by('name')
        return context

class CreateWorkout(CreateView):
    model = models.Workout
    form_class = forms.WorkoutModelForm
    success_url = reverse_lazy("list_workouts")

    def post(self, request, *args, **kwargs):
        obj = self.model(user=request.user)
        form_data = request.POST.copy()
        form = self.get_form(data=form_data, files=request.FILES, instance=obj)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

class UpdateWorkout(UpdateView):
    model = models.Workout
    form_class = forms.WorkoutModelForm
    success_url = reverse_lazy("list_workouts")

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tags'] = ','.join(self.object.tags.all().values_list('name', flat=True))
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_data = request.POST.copy()
        form_data.update(user=self.request.user)
        form = self.get_form(data=form_data, files=request.FILES, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

class DeleteWorkout(DeleteView):
    model = models.Workout
    form_class = forms.WorkoutModelForm
    success_url = reverse_lazy("list_workouts")


class ExerciseListView(ListView):
    model = models.Exercise

    def get_queryset(self):
        return self.model.objects.order_by('name')

class ExerciseCreateView(CreateView):
    model = models.Exercise
    form_class = forms.ExerciseModelForm
    success_url = reverse_lazy("list_exercises")

class ExerciseUpdateeView(UpdateView):
    model = models.Exercise
    form_class = forms.ExerciseModelForm
    success_url = reverse_lazy("list_exercises")

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tags'] = ','.join(self.object.tags.all().values_list('name', flat=True))
        return context

class ExerciseDeleteView(DeleteView):
    model = models.Exercise
    form_class = forms.ExerciseModelForm
    success_url = reverse_lazy("list_exercises")
