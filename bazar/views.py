# bazar/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'bazar/home.html', {'produtos': produtos})

def adicionar_ao_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})

    if str(produto_id) in carrinho:
        carrinho[str(produto_id)] += 1
    else:
        carrinho[str(produto_id)] = 1

    request.session['carrinho'] = carrinho
    return redirect('produtos')

def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    produtos_no_carrinho = []
    total = 0

    for produto_id, quantidade in carrinho.items():
        produto = get_object_or_404(Produto, id=produto_id)
        subtotal = produto.preco * quantidade
        total += subtotal
        produtos_no_carrinho.append({
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': subtotal,
        })
    return render(request, 'carrinho/ver_carrinho.html', {
        'produtos_no_carrinho': produtos_no_carrinho,
        'total': total,
    })

def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})

    if str(produto_id) in carrinho:
        del carrinho[str(produto_id)]
        request.session['carrinho'] = carrinho
    
    return redirect('carrinho_produtos')

def detalhes_do_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    context = {
        'produto': produto
    }
    return render(request, 'bazar/detalhes_do_produto.html', context)

def atualizar_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    
    if request.method == 'POST':
        for produto_id, quantidade in request.POST.items():
            if produto_id.isdigit():
                if int(quantidade) > 0:
                    carrinho[produto_id] = int(quantidade)
                else:
                    del carrinho[produto_id]
        request.session['carrinho'] = carrinho
    return redirect('carrinho_produtos')