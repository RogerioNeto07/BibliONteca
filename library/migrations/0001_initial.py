# Generated by Django 5.1.4 on 2025-02-22 15:55

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Livro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200)),
                ("subtitulo", models.CharField(blank=True, max_length=200, null=True)),
                ("editora", models.CharField(max_length=50)),
                ("autor", models.CharField(max_length=100)),
                ("volume", models.IntegerField(blank=True, null=True)),
                ("idioma", models.CharField(max_length=20)),
                ("qntd_paginas", models.IntegerField()),
                ("classificacao", models.IntegerField()),
                ("descricao", models.CharField(max_length=500)),
                ("isbn", models.CharField(max_length=13, unique=True)),
                ("ano_publicacao", models.IntegerField()),
                ("capa", models.ImageField(upload_to="capas/")),
                ("data_cadastro", models.DateField(auto_now_add=True)),
                ("quantidade", models.IntegerField(default=1)),
                (
                    "categoria",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.categoria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Emprestimo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_emprestimo", models.DateField(default=datetime.date.today)),
                ("previsao_devolucao", models.DateField()),
                ("data_devolucao", models.DateField(blank=True, null=True)),
                ("status_ativo", models.BooleanField(default=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emprestimos",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "livro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emprestimos",
                        to="library.livro",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comentarios",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comentario", models.TextField(blank=True)),
                ("estrela", models.PositiveBigIntegerField()),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "livro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        to="library.livro",
                    ),
                ),
            ],
        ),
    ]
