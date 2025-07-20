from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    CATEGORIAS = [
        ('INFANTIL', 'Infantil'),
        ('FEMININO', 'Feminino'),
        ('MASCULINO', 'Masculino'),
        ('CALÇADOS', 'Calçados'),
        ('OUTROS', 'Outros'),
    ]
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='OUTROS')

    def __str__(self):
        return self.nome
