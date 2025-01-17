from django.db import models

class Leitor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    rua = models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.nome
