# Generated by Django 4.1.4 on 2022-12-19 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_fk_produto_imagesproduto_fkproduto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesproduto',
            options={'verbose_name_plural': 'Imagens do produto'},
        ),
    ]
