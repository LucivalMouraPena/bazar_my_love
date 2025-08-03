from django.shortcuts import render, redirect, get_object_or_404
from bazar.models import Produto

def home(request):
    return render(request, 'bazar/home.html')

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
