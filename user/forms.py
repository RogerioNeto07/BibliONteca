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
                'email': forms.EmailInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título'}),
                'nome': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título'}),
                'cpf': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título'}),
                'data_nascimento': forms.DateInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título', 'type': 'date'}),
                'telefone': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título'}),
                'bairro': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título'}),
                'rua': forms.TextInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título'}),
                'numero': forms.NumberInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título'}),
                'foto_perfil': forms.FileInput(attrs={'class': 'input-form secundary-text bold', 'placeholder': 'Título'}),
            }

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
