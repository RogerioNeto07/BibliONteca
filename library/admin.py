from django.contrib import admin
from .models import Emprestimo, Livro, Categoria, Comentarios


admin.site.register(Livro)
admin.site.register(Categoria)
admin.site.register(Emprestimo)
admin.site.register(Comentarios)
