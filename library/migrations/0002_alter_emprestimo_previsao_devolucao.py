# Generated by Django 5.1.4 on 2025-02-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emprestimo",
            name="previsao_devolucao",
            field=models.DateField(blank=True),
        ),
    ]
