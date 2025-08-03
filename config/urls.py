"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatt erns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from bazar import views as bazar_views
from carrinho import views as carrinho_views  # Se tiver uma app 'carrinho'

urlpatterns = [
    path('admin/', admin.site.urls),  # painel admin

    path('', bazar_views.home, name='home'),  # página principal
    path('produtos/', bazar_views.home, name='produtos'),


    path('carrinho/produtos/', bazar_views.carrinho_produtos, name='carrinho_produtos'),
    path('adicionar/<int:produto_id>/', bazar_views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', bazar_views.remover_do_carrinho, name='remover_do_carrinho'),
    path('atualizar/', bazar_views.atualizar_carrinho, name='atualizar_carrinho'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
