from django.db import migrations


def set_product_images(apps, schema_editor):
    Produto = apps.get_model('bazar', 'Produto')
    mapping = {
        'Vestido Floral': 'produtos/vestido_floral.svg',
        'Camiseta Básica': 'produtos/camiseta_basica.svg',
        'Short Jeans': 'produtos/short_jeans.svg',
        'Sandália Rasteira': 'produtos/sandalia_rasteira.svg',
        'Conjunto Infantil': 'produtos/conjunto_infantil.svg',
        'Jaqueta Jeans': 'produtos/jaqueta_jeans.svg',
        'Blusa de Tricô': 'produtos/blusa_de_trico.svg',
        'Tênis Casual': 'produtos/tenis_casual.svg',
        'Vestido Infantil': 'produtos/vestido_infantil.svg',
        'Bolsa Tiracolo': 'produtos/bolsa_tiracolo.svg',
    }
    for nome, imagem in mapping.items():
        produto = Produto.objects.filter(nome=nome).first()
        if produto:
            produto.imagem.name = imagem
            produto.save(update_fields=['imagem'])


def unset_product_images(apps, schema_editor):
    Produto = apps.get_model('bazar', 'Produto')
    nomes = [
        'Vestido Floral', 'Camiseta Básica', 'Short Jeans', 'Sandália Rasteira',
        'Conjunto Infantil', 'Jaqueta Jeans', 'Blusa de Tricô', 'Tênis Casual',
        'Vestido Infantil', 'Bolsa Tiracolo',
    ]
    Produto.objects.filter(nome__in=nomes).update(imagem='')


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0006_load_sample_products'),
    ]

    operations = [
        migrations.RunPython(set_product_images, unset_product_images),
    ]
