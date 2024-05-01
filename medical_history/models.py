from django.db import models
from accounts.models import User
from attendance_sheet.models import AttendanceSheet


class MedicalCareHistory(models.Model):
    attendance_sheet = models.OneToOneField(
        AttendanceSheet,
        on_delete=models.CASCADE,
        related_name="medical_care_history",
        verbose_name="Ficha de Atendimento",
    )

    doctor_attended = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_attended",
        verbose_name="Médico(a) que Atendeu"
    )

    service_date = models.DateTimeField(verbose_name="Data do Atendimento", auto_now_add=True)

    class Meta:
        verbose_name = "Histórico de Atendimento"
        verbose_name_plural = "Históricos de Atendimento"
        ordering = ["service_date"]
        db_table = "medical_care_histories"

    def __str__(self):
        return f'({self.doctor_attended}) - {self.attendance_sheet}'
