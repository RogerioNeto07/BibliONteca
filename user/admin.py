from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ("email", "nome", "is_active", "is_staff")
    search_fields = ("email", "nome", "cpf")
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações pessoais", {"fields": ("nome", "cpf", "data_nascimento", "telefone")}),
        ("Endereço", {"fields": ("bairro", "rua", "numero")}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "nome", "cpf", "data_nascimento", "telefone", "bairro", "rua", "numero", "password1", "password2", "is_active", "is_staff"),
        }),
    )

    list_filter = ("is_staff", "is_active")

