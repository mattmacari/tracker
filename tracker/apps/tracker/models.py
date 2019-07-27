from django.db import models
from django.contrib.auth.models import User


# #######################################
# Weight Tracker Models
# #######################################


class Weight(models.Model):

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete="cascade", db_index=True)
    measured_date = models.DateTimeField()
    weight = models.FloatField()
    scale_calc_body_fat = models.FloatField(null=True, blank=True)
    scale_calc_lbm = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Weight"