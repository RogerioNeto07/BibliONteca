from django.db import models
from django.contrib.auth.models import AbstractUser

class Leitor(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='leitor',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='leitor_permissions',
        blank=True,
    )