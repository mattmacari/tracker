import json

from dateutil import parser
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from vanilla import CreateView, DeleteView, ListView, UpdateView

from . import forms, models, services


def index(request):
    return render(request, "tracker/base.html")


class ListWeights(ListView):
    model = models.Weight

    def get_queryset(self):
        return models.Weight.objects.filter(user=self.request.user).order_by(
            "measured_date"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dates, weights = services.get_weight_timeseries(user=self.request.user)
        context["plot_dates"] = json.dumps([elem.strftime('%Y-%m-%d') for elem in dates])
        context["plot_weights"] = list(weights)
        return context


class CreateWeight(CreateView):
    model = models.Weight
    form_class = forms.WeightForm
    success_url = reverse_lazy("list_weight")

    def post(self, request, *args, **kwargs):
        obj = self.model(user=request.user)
        form_data = request.POST.copy()
        form_data.update(
            {"measured_date": parser.parse(form_data.get("measured_date"))}
        )
        form = self.get_form(data=form_data, files=request.FILES, instance=obj)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)


class UpdateWeight(UpdateView):
    model = models.Weight
    form_class = forms.WeightForm
    success_url = reverse_lazy("list_weight")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_data = request.POST.copy()
        form_data.update(
            {
                "measured_date": parser.parse(form_data.get("measured_date")),
                "user": request.user,
            }
        )
        form = self.get_form(data=form_data, files=request.FILES, instance=self.object)
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)


class DeleteWeight(DeleteView):
    model = models.Weight
    success_url = reverse_lazy("list_weight")
