from django.db import models
from django.contrib.auth.models import User
from common.models import TimeStampedModel


class Patient(TimeStampedModel):

    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
        OTHER = "Other", "Other"

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="patients"
    )

    name = models.CharField(max_length=150)

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )

    phone = models.CharField(max_length=15)

    address = models.TextField()

    def __str__(self):
        return self.name