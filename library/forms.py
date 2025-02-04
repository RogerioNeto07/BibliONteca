from django import forms
from books.models import Livro
from user.models import Leitor
from .models import Emprestimo

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = [
            'titulo', 'subtitulo', 'editora', 'autor', 'volume', 'idioma', 
            'categoria', 'qntd_paginas', 'classificacao', 'descricao', 'isbn', 
            'ano_publicacao', 'capa'
        ]

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['leitor', 'livro']