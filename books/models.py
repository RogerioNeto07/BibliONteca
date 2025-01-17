from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    subtitulo = models.CharField(max_length=200)
    editora = models.CharField(max_length=50)
    autor = models.CharField(max_length=100, null=False, blank=False)
    volume = models.IntegerField(null=False, blank=False)
    idioma = models.CharField(max_length=20, null=False, blank=False)
    categoria = models.CharField(max_length=100)
    qntd_paginas = models.IntegerField(null=False, blank=False)
    classificacao = models.IntegerField(null=False, blank=False)
    descricao = models.CharField(max_length=500, null=False, blank=False)
    isbn = models.CharField(max_length=13, unique=True, null=False, blank=False)
    ano_publicacao = models.IntegerField(null=False, blank=False)
    capa = models.ImageField(upload_to="capas/", null=False, blank=False)


    def __str__(self):
        return self.titulo

