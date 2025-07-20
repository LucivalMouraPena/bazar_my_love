from django.shortcuts import render
from .models import Produto

def home(request):
    produtos = Produto.objects.all()  # pega todos os produtos do banco
    return render(request, 'bazar/home.html', {'produtos': produtos})
def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'bazar/produtos.html', {'produtos': produtos})