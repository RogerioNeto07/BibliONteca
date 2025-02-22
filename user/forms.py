from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser

class UserRegisterForm(UserCreationForm):
        password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Digite sua senha'})
        )
        password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Confirme sua senha'})
        )

        class Meta:
            model = MyUser
            fields = ['email', 'nome', 'cpf', 'data_nascimento', 'telefone', 'bairro', 'rua', 'numero', 'foto_perfil', 'password1', 'password2']
            widgets = {
                'email': forms.EmailInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'E-mail'}),
                'nome': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Nome'}),
                'cpf': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': '999.888.777-66'}),
                'data_nascimento': forms.DateInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título', 'type': 'date'}),
                'telefone': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': '(99) 99999-9999'}),
                'bairro': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Bairro'}),
                'rua': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Rua'}),
                'numero': forms.NumberInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Numero'}),
                'foto_perfil': forms.FileInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título'}),
            }

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
