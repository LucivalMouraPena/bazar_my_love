
from django.shortcuts import render
from .models import Produto

def home(request):
    produtos = Produto.objects.all()  # pega todos os produtos do banco
    return render(request, 'bazar/home.html', {'produtos': produtos})
def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'bazar/produtos.html', {'produtos': produtos})

from django.shortcuts import redirect, get_object_or_404
from bazar.models import Produto
from django.shortcuts import render

def home(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'bazar/home.html', {'produtos': lista_produtos})


def atualizar_carrinho(request):
    if request.method == 'POST':
        carrinho = request.session.get('carrinho', {})
        for produto_id, quantidade in request.POST.items():
            if produto_id.startswith('quantidade_'):
                pid = produto_id.split('_')[1]
                if quantidade.isdigit() and int(quantidade) > 0:
                    carrinho[pid] = int(quantidade)
                else:
                    if pid in carrinho:
                        del carrinho[pid]
        request.session['carrinho'] = carrinho
    return redirect('carrinho_produtos')

def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    if str(produto_id) in carrinho:
        del carrinho[str(produto_id)]
    request.session['carrinho'] = carrinho
    return redirect('carrinho_produtos')

def carrinho_produtos(request):
    carrinho = request.session.get('carrinho', {})
    produtos = []

    for produto_id, quantidade in carrinho.items():
        produto = Produto.objects.get(id=produto_id)
        produtos.append((produto, quantidade))

    return render(request, 'bazar/carrinho.html', {'produtos': produtos})
from django.shortcuts import redirect

def adicionar_ao_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    carrinho[str(produto_id)] = carrinho.get(str(produto_id), 0) + 1
    request.session['carrinho'] = carrinho
    return redirect('carrinho_produtos')

