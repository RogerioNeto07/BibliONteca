from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='perfil/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  

    def __str__(self):
        return self.email
