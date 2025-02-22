from django import forms
from .models import Livro, Categoria

from .models import Emprestimo

class LivroForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
        empty_label="Selecione uma categoria",
        widget=forms.Select(attrs={'class': 'input-form'}))

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
        fields = ['usuario', 'livro']
        widgets = {
            'usuario': forms.TextInput(attrs={
                'class': 'input secundary-text bold',
                'placeholder': '999.999.999-99'
            }),
            'livro': forms.TextInput(attrs={
                'class': 'input secundary-text bold',
                'placeholder': 'Código do livro'
            })
        }

class DevolucaoForm(forms.Form):
    nome = forms.CharField(label="Usuário", max_length=200, required=True)
    isbn = forms.CharField(label="ISBN", max_length=13, required=True)

class RenovarForm(forms.Form):
    nome = forms.CharField(label="Nome do usuário", max_length=200, required=True)
    isbn = forms.CharField(label="ISBN", max_length=13, required=True)
