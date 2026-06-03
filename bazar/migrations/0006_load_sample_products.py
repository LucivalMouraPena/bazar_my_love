from django.db import migrations


def create_sample_products(apps, schema_editor):
    Produto = apps.get_model('bazar', 'Produto')

    sample_products = [
        {
            'nome': 'Vestido Floral',
            'estoque': 12,
            'descricao': 'Vestido leve com estampa floral para ocasiões casuais.',
            'preco': '159.90',
            'categoria': 'FEMININO',
        },
        {
            'nome': 'Camiseta Básica',
            'estoque': 25,
            'descricao': 'Camiseta de algodão confortável para uso diário.',
            'preco': '49.90',
            'categoria': 'MASCULINO',
        },
        {
            'nome': 'Short Jeans',
            'estoque': 15,
            'descricao': 'Short jeans com acabamento moderno e bolsos funcionais.',
            'preco': '89.90',
            'categoria': 'OUTROS',
        },
        {
            'nome': 'Sandália Rasteira',
            'estoque': 18,
            'descricao': 'Sandália rasteira com tiras confortáveis para o dia a dia.',
            'preco': '79.90',
            'categoria': 'CALCADOS',
        },
        {
            'nome': 'Conjunto Infantil',
            'estoque': 20,
            'descricao': 'Conjunto infantil macio e colorido para brincar com estilo.',
            'preco': '69.90',
            'categoria': 'INFANTIL',
        },
        {
            'nome': 'Jaqueta Jeans',
            'estoque': 10,
            'descricao': 'Jaqueta jeans clássica que combina com várias produções.',
            'preco': '219.90',
            'categoria': 'MASCULINO',
        },
        {
            'nome': 'Blusa de Tricô',
            'estoque': 14,
            'descricao': 'Blusa de tricô quentinha para dias mais frios.',
            'preco': '129.90',
            'categoria': 'FEMININO',
        },
        {
            'nome': 'Tênis Casual',
            'estoque': 22,
            'descricao': 'Tênis casual confortável com solado leve.',
            'preco': '179.90',
            'categoria': 'CALCADOS',
        },
        {
            'nome': 'Vestido Infantil',
            'estoque': 16,
            'descricao': 'Vestido infantil delicado com acabamento em renda.',
            'preco': '89.90',
            'categoria': 'INFANTIL',
        },
        {
            'nome': 'Bolsa Tiracolo',
            'estoque': 13,
            'descricao': 'Bolsa tiracolo prática para levar o essencial com estilo.',
            'preco': '99.90',
            'categoria': 'OUTROS',
        },
    ]

    for produto_data in sample_products:
        Produto.objects.update_or_create(
            nome=produto_data['nome'],
            defaults=produto_data,
        )


def remove_sample_products(apps, schema_editor):
    Produto = apps.get_model('bazar', 'Produto')
    nomes = [
        'Vestido Floral',
        'Camiseta Básica',
        'Short Jeans',
        'Sandália Rasteira',
        'Conjunto Infantil',
        'Jaqueta Jeans',
        'Blusa de Tricô',
        'Tênis Casual',
        'Vestido Infantil',
        'Bolsa Tiracolo',
    ]
    Produto.objects.filter(nome__in=nomes).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0005_alter_produto_options_produto_criado_em_and_more'),
    ]

    operations = [
        migrations.RunPython(create_sample_products, remove_sample_products),
    ]
