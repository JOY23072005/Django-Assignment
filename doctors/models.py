from django.db import models
from common.models import TimeStampedModel


class Doctor(TimeStampedModel):

    name = models.CharField(max_length=150)

    specialization = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    experience = models.PositiveIntegerField(
        help_text="Experience in years"
    )

    def __str__(self):
        return f"{self.name} ({self.specialization})"