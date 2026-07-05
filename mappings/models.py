from django.db import models

from patients.models import Patient
from doctors.models import Doctor
from common.models import TimeStampedModel


class PatientDoctorMapping(TimeStampedModel):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="doctor_mappings"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="patient_mappings"
    )

    class Meta:
        unique_together = ("patient", "doctor")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.patient.name} → {self.doctor.name}"