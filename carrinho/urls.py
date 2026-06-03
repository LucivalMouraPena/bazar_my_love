from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrinho, name='carrinho_produtos'),
]
