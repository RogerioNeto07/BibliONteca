from django.db import models
from user.models import Leitor
from books.models import Livro
from datetime import date, timedelta

class Emprestimo(models.Model):
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE, related_name="emprestimos")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="emprestimos")
    data_emprestimo = models.DateField(auto_now_add=True)
    previsao_devolucao = models.DateField(null=False, blank=False)
    data_devolucao = models.DateField(null=True, blank=True)
    status_ativo = models.BooleanField(default=True)
    renovacoes = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.previsao_devolucao:
            self.previsao_devolucao = self.data_emprestimo + timedelta(days=15)
        super().save(*args, **kwargs)

    def renovar(self):
        if self.renovacoes < 3:
            self.data_devolucao += timedelta(days=15)
            self.renovacoes += 1
            self.save()
            return True
        return False
    

    def devolver_livro(self):
        self.status_ativo = False
        self.save()


    def __str__(self):
        return f"{self.leitor.nome} - {self.livro.titulo}"