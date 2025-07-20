from django.contrib import admin
from django.utils.html import format_html
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'imagem_preview')
    list_filter = ()

    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="50" />', obj.imagem.url)
        return "-"
    imagem_preview.short_description = 'Imagem'

admin.site.register(Produto, ProdutoAdmin)
