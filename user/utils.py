from .models import Notificacao
from django.utils.timezone import now
from library.models import Emprestimo
from django.core.cache import cache

def adicionar_notificacao(usuario, mensagem, tipo="geral"):
    Notificacao.objects.create(
        usuario=usuario,
        mensagem=mensagem,
        tipo=tipo,
    )

def verificar_emprestimos_vencidos():
    cache_key = "emprestimos_vencidos"
    if cache.get(cache_key) is None:
        emprestimos_vencidos = Emprestimo.objects.filter(previsao_devolucao=now().date(), status_ativo=True)
        
        for emprestimo in emprestimos_vencidos:
            mensagem = f"O livro '{emprestimo.livro.titulo}' precisa ser devolvido hoje!"
            Notificacao.objects.create(usuario=emprestimo.usuario, mensagem=mensagem, tipo="pendencia")

        cache.set(cache_key, "verificado", timeout=1)

