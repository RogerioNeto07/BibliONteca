from django.db import models
from user.models import Leitor
from books.models import Livro
from datetime import date, timedelta

class Emprestimo(models.Model):
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE, related_name="emprestimos")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="emprestimos")
    data_emprestimo = models.DateField(default=date.today)
    previsao_devolucao = models.DateField(null=False, blank=False)
    data_devolucao = models.DateField(null=True, blank=True)
    status_ativo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.previsao_devolucao:
            self.previsao_devolucao = self.data_emprestimo + timedelta(days=15)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.leitor.nome} - {self.livro.titulo}"
