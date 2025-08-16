from django.db import models

class Produto(models.Model):
    CATEGORIAS = [
        ('INFANTIL', 'Infantil'),
        ('FEMININO', 'Feminino'),
        ('MASCULINO', 'Masculino'),
        ('CALÇADOS', 'Calçados'),
        ('OUTROS', 'Outros'),
    ]

    nome = models.CharField(max_length=100, unique=True)
    estoque = models.PositiveIntegerField(default=0)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='OUTROS')

    class Meta:
        ordering = ['nome']  # ou ['preco'] se preferir
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    @classmethod
    def filtrar_por_categoria(cls, categoria):
        return cls.objects.filter(categoria=categoria)

    def __str__(self):
        return self.nome
