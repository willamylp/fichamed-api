from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import User


class Classification(models.TextChoices):
    RED = "Red", "Vermelho"
    ORANGE = "Orange", "Laranja"
    YELLOW = "Yellow", "Amarelo"
    GREEN = "Green", "Verde"
    BLUE = "Blue", "Azul"
    IGNORED = "Ignored", "Ignorado"


class AttendanceSheet(models.Model):

    filled_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="filled_by",
        verbose_name="Preenchido por"
    )

    card_number = models.IntegerField(
        verbose_name="Número da Ficha",
        validators=[
            MinValueValidator(1, "O número da ficha deve ser maior que 0.")
        ]
    )
    patient_name = models.CharField(verbose_name="Nome do Paciente", max_length=255)

    clinical_history = models.TextField(
        verbose_name="História Clínica",
        max_length=500,
        blank=True,
        null=True
    )
    classification = models.CharField(
        verbose_name="Classificação",
        max_length=10,
        choices=Classification.choices,
    )

    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Ficha de Atendimento"
        verbose_name_plural = "Fichas de Atendimento"
        ordering = ["-created_at"]
        db_table = "attendance_sheets"

    def __str__(self):
        return f'[{self.card_number}] - {self.patient_name}'
