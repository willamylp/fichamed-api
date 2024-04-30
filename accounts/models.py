from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None
    last_name = None
    date_joined = None

    full_name = models.CharField(verbose_name="Nome Completo", max_length=255)
    username = models.CharField(verbose_name="Nome de Usuário", max_length=255, unique=True)
    email = models.EmailField(verbose_name="E-mail", max_length=255)

    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)

    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    is_staff = models.BooleanField(verbose_name="Admin", default=False)
    is_superuser = models.BooleanField(verbose_name="Superusuário", default=False)

    REQUIRED_FIELDS = ['email', 'full_name']
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.full_name
