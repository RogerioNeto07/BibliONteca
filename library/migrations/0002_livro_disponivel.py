# Generated by Django 5.1.3 on 2025-02-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
