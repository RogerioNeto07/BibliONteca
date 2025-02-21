from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Livro
from datetime import date

class Leitor(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    nome = models.CharField(max_length=255)
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)

    def __str__(self):
        return self.cpf + " - " + self.nome

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

class Avaliacao(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=False, blank=False, related_name="avaliacoes")
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE, null=False, blank=False, related_name="avaliacoes")
    data_emprestimo = models.DateField(default=date.today)
    nota = models.IntegerField(null=False, blank=False)
    comentario = models.CharField(max_length=2500, null=True, blank=True)

    def __str__(self):
        return f"{self.leitor.nome} - {self.livro.titulo}"