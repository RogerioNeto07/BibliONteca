# Generated by Django 5.1.3 on 2025-01-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_leitor_options_alter_leitor_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leitor',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
