# Generated by Django 5.1.4 on 2025-02-21 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("library", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="emprestimo",
            name="usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="emprestimos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="livro",
            name="categoria",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="library.categoria",
            ),
        ),
        migrations.AddField(
            model_name="emprestimo",
            name="livro",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="emprestimos",
                to="library.livro",
            ),
        ),
    ]
