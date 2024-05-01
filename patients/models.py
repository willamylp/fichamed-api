from django.db import models


class Patient(models.Model):
    patient_name = models.CharField(verbose_name="Nome do Paciente", max_length=255)
    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.patient_name
