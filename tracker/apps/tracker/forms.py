from django import forms

from . import models


class WeightForm(forms.ModelForm):
    class Meta:
        model = models.Weight
        fields = ["measured_date", "weight", "scale_calc_body_fat", "scale_calc_lbm"]

