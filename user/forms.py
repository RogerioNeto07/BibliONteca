from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['email', 'nome', 'cpf', 'data_nascimento', 'telefone', 'bairro', 'rua', 'numero', 'foto_perfil', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
