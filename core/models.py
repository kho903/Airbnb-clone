from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """Time Stamped Model"""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManger()

    class Meta:
        abstract = True