from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Leitor, Avaliacao

class LeitorForm(UserCreationForm):
    class Meta:
        model = Leitor
        fields = ['cpf', 'email', 'data_nascimento', 'telefone', 'bairro', 'rua', 'numero','nome']
    
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirmar senha')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não são iguais.")
        return password2

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']
        