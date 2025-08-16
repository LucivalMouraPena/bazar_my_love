from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from bazar import views as bazar_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Páginas do bazar
    path('', bazar_views.home, name='home'),                # página principal (lista produtos)
    path('produtos/', bazar_views.home, name='produtos'),   # aponta para a mesma view da home

    # Carrinho (usando as views do app bazar)
    path('carrinho/produtos/', bazar_views.carrinho_produtos, name='carrinho_produtos'),
    path('adicionar/<int:produto_id>/', bazar_views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', bazar_views.remover_do_carrinho, name='remover_do_carrinho'),
    path('atualizar/', bazar_views.atualizar_carrinho, name='atualizar_carrinho'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

