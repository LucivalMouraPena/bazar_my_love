@'
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto


def home(request):
    produtos = Produto.objects.all()
    return render(request, 'bazar/home.html', {'produtos': produtos})


def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = request.session.get('carrinho', {})
    chave = str(produto_id)

    quantidade_atual = carrinho.get(chave, 0)

    if quantidade_atual >= produto.estoque:
        messages.warning(request, f'Estoque insuficiente para "{produto.nome}".')
        return redirect('home')

    carrinho[chave] = quantidade_atual + 1
    request.session['carrinho'] = carrinho
    return redirect('home')


def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    produtos_no_carrinho = []
    total = 0

    ids = [int(pid) for pid in carrinho.keys()]
    produtos = {str(p.id): p for p in Produto.objects.filter(id__in=ids)}

    for produto_id, quantidade in carrinho.items():
        produto = produtos.get(produto_id)
        if produto is None:
            continue
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


def detalhes_do_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'bazar/detalhes_do_produto.html', {'produto': produto})


def atualizar_carrinho(request):
    if request.method != 'POST':
        return redirect('carrinho_produtos')

    carrinho = request.session.get('carrinho', {})

    for produto_id, quantidade_str in request.POST.items():
        if not produto_id.isdigit():
            continue

        try:
            quantidade = int(quantidade_str)
        except (ValueError, TypeError):
            continue

        produto = Produto.objects.filter(id=produto_id).first()
        if produto is None:
            carrinho.pop(produto_id, None)
            continue

        if quantidade > produto.estoque:
            quantidade = produto.estoque
            messages.warning(request, f'Quantidade de "{produto.nome}" ajustada ao estoque disponivel.')

        if quantidade > 0:
            carrinho[produto_id] = quantidade
        else:
            carrinho.pop(produto_id, None)

    request.session['carrinho'] = carrinho
    return redirect('carrinho_produtos')


def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    carrinho.pop(str(produto_id), None)
    request.session['carrinho'] = carrinho
    return redirect('carrinho_produtos')
'@ | Set-Content bazar\views.py -Encoding UTF8