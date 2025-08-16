# carrinho/urls.py
from django.urls import path
from bazar import views as bazar_views
from . import views

from django.urls import include, path

urlpatterns = [
    path('', include('bazar.urls')),
    path('carrinho/', include('carrinho.urls')),  # <-- essa linha
    path('admin/', admin.site.urls),
]
