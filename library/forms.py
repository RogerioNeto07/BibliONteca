from django import forms
from .models import Livro, Categoria, Emprestimo
from user.models import MyUser

class LivroForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        empty_label="Selecione uma categoria",
        widget=forms.Select(attrs={'class': 'input-form'})
    )

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
        widgets = {
            'leitor': forms.TextInput(attrs={
                'class': 'input secundary-text bold',
                'placeholder': '999.999.999-99'
            }),
            'livro': forms.TextInput(attrs={
                'class': 'input secundary-text bold',
                'placeholder': 'Código do livro'
            })
        }


class RenovarForm(forms.Form):
    usuario = forms.ModelChoiceField(
        queryset=MyUser.objects.all(),
        label="Usuário",
        required=True
    )
    emprestimo = forms.ModelChoiceField(
        queryset=Emprestimo.objects.none(),
        label="Selecione o Empréstimo",
        required=True
    )

    def salvar(self):
        emprestimo = self.cleaned_data['emprestimo']
        if emprestimo.renovar():
            emprestimo.save()
            return True
        return False


class DevolucaoForm(forms.Form):
    usuario = forms.ModelChoiceField(
        queryset=MyUser.objects.all(),
        label="Usuário",
        required=True
    )
    emprestimo = forms.ModelChoiceField(
        queryset=Emprestimo.objects.filter(status_ativo=False),
        label="Selecione o Empréstimo",
        required=True
    )

    def salvar(self):
        emprestimo = self.cleaned_data['emprestimo']
        emprestimo.devolver_livro()
        emprestimo.save()
