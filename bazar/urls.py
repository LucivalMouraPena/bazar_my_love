from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produto/<int:produto_id>/', views.detalhes_do_produto, name='detalhes'),
    path('carrinho/', views.ver_carrinho, name='carrinho_produtos'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('atualizar/', views.atualizar_carrinho, name='atualizar_carrinho'),
    path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]
