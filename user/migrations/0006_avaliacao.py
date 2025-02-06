# Generated by Django 5.1.3 on 2025-02-06 13:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_categoria_alter_livro_categoria'),
        ('user', '0005_alter_leitor_foto_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField(default=datetime.date.today)),
                ('nota', models.IntegerField()),
                ('comentario', models.CharField(blank=True, max_length=2500, null=True)),
                ('leitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.leitor')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.livro')),
            ],
        ),
    ]
