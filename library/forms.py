from django import forms
from .models import Livro, Categoria, Emprestimo
from django.contrib.auth.forms import UserChangeForm
from user.models import MyUser
from django.core.exceptions import ValidationError


class LivroForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
        empty_label="Selecione uma categoria",
        widget=forms.Select(attrs={'class': 'input-form'}))

    class Meta:
        model = Livro
        fields = [
            'titulo', 'subtitulo', 'editora', 'autor', 'volume', 'idioma', 
            'categoria', 'qntd_paginas', 'classificacao', 'descricao', 'isbn', 
            'ano_publicacao', 'capa', 'quantidade'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título'}),
            'subtitulo': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Sub-título'}),
            'categoria': forms.Select(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Categoria'}),
            'autor': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Autor'}),
            'idioma': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Idioma'}),
            'capa': forms.ClearableFileInput(attrs={'class': 'input-form secundary-text bold'}),
            'descricao': forms.Textarea(attrs={'class': 'input-form secundary-text bold input-description', 'placeholder': 'Descrição'}),
            'classificacao': forms.TextInput(attrs={'class': 'input-form secundary-text bold width-three', 'placeholder': 'Faixa Étaria'}),
            'ano_publicacao': forms.NumberInput(attrs={'class': 'input-form secundary-text bold width-three', 'placeholder': 'Ano'}),
            'qntd_paginas': forms.NumberInput(attrs={'class': 'input-form secundary-text bold width-three', 'placeholder': 'Quantidade'}),
            'isbn': forms.TextInput(attrs={'class': 'input-form secundary-text bold width-one', 'placeholder': 'ISBN'}),
            'editora': forms.TextInput(attrs={'class': 'input-form secundary-text bold width-one', 'placeholder': 'Editora'}),
            'volume': forms.TextInput(attrs={'class': 'input-form secundary-text bold width-two', 'placeholder': 'Volume'}),
            'quantidade' : forms.TextInput(attrs={'class': 'input-form secundary-text bold width-two', 'placeholder': 'Quantidade'})
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro']

    usuario = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input secundary-text bold',
            'placeholder': '999.999.999-99'
        })
    )

    livro = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input secundary-text bold',
            'placeholder': 'Código do livro'
        })
    )

    def clean_usuario(self):
        cpf = self.cleaned_data['usuario'].strip()
        
        usuario = MyUser.objects.get(cpf=cpf)
        return usuario

    def clean_livro(self):
        codigo = self.cleaned_data['livro'].strip()
        livro = Livro.objects.get(isbn=codigo)
        return livro

class DevolucaoForm(forms.Form):
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro']
    
    usuario = forms.CharField(
                label="Usuário", 
                max_length=200, 
                required=True, 
                widget=forms.TextInput(
                attrs={
                    'class': 'input secundary-text bold',
                    'placeholder': 'CPF'
            })
        )
    livro = forms.CharField(
                label="ISBN", 
                max_length=13, 
                required=True, 
                widget=forms.TextInput(
                attrs={
                    'class': 'input secundary-text bold',
                    'placeholder': 'ISBN'
            })
        )


    def clean_usuario(self):
        cpf = self.cleaned_data['usuario'].strip()
        
        usuario = MyUser.objects.get(cpf=cpf)
        return usuario

    def clean_livro(self):
        codigo = self.cleaned_data['livro'].strip()
        livro = Livro.objects.get(isbn=codigo)
        return livro


class RenovarForm(forms.Form):
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro']
    
    usuario = forms.CharField(
                label="Usuário", 
                max_length=200, 
                required=True, 
                widget=forms.TextInput(
                attrs={
                    'class': 'input secundary-text bold',
                    'placeholder': 'CPF'
            })
        )
    livro = forms.CharField(
                label="ISBN", 
                max_length=13, 
                required=True, 
                widget=forms.TextInput(
                attrs={
                    'class': 'input secundary-text bold',
                    'placeholder': 'ISBN'
            })
        )

    def clean_usuario(self):
        cpf = self.cleaned_data['usuario'].strip()
        
        usuario = MyUser.objects.get(cpf=cpf)
        return usuario

    def clean_livro(self):
        codigo = self.cleaned_data['livro'].strip()
        livro = Livro.objects.get(isbn=codigo)
        return livro
    
        
class UsuarioUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = MyUser
        fields = ['nome', 'cpf', 'email', 'data_nascimento', 'telefone', 'bairro', 'rua', 'numero']
