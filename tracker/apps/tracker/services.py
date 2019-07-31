import datetime
import typing

from django.contrib.auth.models import User
from django.utils import timezone

from . import models


def get_weight_timeseries(
    user: User,
    min_dt: typing.Optional[timezone.datetime] = None,
    max_dt: typing.Optional[timezone.datetime] = None,
) -> typing.Tuple[typing.List, ...]:
    """

    """
    dates = (
        models.Weight.objects.filter(user=user)
        .values_list("measured_date", flat=True)
        .order_by("measured_date")
    )
    weights = (
        models.Weight.objects.filter(user=user)
        .values_list("weight", flat=True)
        .order_by("measured_date")
    )

    if all([min_dt, max_dt]):
        dates = dates.filter(measured_date__range=(min_dt, max_dt))
        weights = weights.filter(measured_date__range=(min_dt, max_dt))

    return (dates, weights)
