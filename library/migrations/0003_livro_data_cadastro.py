# Generated by Django 5.1.6 on 2025-02-22 11:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
