from django.db import models
from user.models import MyUser 
from datetime import timedelta
    

class Categoria(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    subtitulo = models.CharField(max_length=200)
    editora = models.CharField(max_length=50)
    autor = models.CharField(max_length=100, null=False, blank=False)
    volume = models.IntegerField(null=False, blank=False)
    idioma = models.CharField(max_length=20, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default="")
    qntd_paginas = models.IntegerField(null=False, blank=False)
    classificacao = models.IntegerField(null=False, blank=False)
    descricao = models.CharField(max_length=500, null=False, blank=False)
    isbn = models.CharField(max_length=13, unique=True, null=False, blank=False)
    ano_publicacao = models.IntegerField(null=False, blank=False)
    capa = models.ImageField(upload_to="capas/", null=False, blank=False)
    data_cadastro = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.titulo
    

class Emprestimo(models.Model):
    usuario = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="emprestimos")  
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="emprestimos")
    data_emprestimo = models.DateField(auto_now_add=True)
    previsao_devolucao = models.DateField(null=False, blank=False)
    data_devolucao = models.DateField(null=True, blank=True)
    status_ativo = models.BooleanField(default=True)
    renovacoes = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.previsao_devolucao:
            self.previsao_devolucao = self.data_emprestimo + timedelta(days=15)
        super().save(*args, **kwargs)

    def renovar(self):
        if self.renovacoes < 3:
            self.data_devolucao += timedelta(days=15)
            self.renovacoes += 1
            self.save()
            return True
        return False
    

    def devolver_livro(self):
        self.status_ativo = False
        self.save()


    def __str__(self):
        return f"{self.usuario.email} - {self.livro.titulo}"  


