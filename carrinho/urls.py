# carrinho/urls.py
from django.urls import path
from bazar import views as bazar_views
from . import views

urlpatterns = [
    path('', bazar_views.home, name='home'),
    path('produtos/', bazar_views.produtos, name='produtos'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('ver/', views.ver_carrinho, name='ver_carrinho'),
]
