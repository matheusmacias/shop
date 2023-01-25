# Generated by Django 4.1.4 on 2022-12-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_produto_image_alter_produto_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='image',
        ),
        migrations.AddField(
            model_name='produto',
            name='imagemain',
            field=models.ImageField(default='', upload_to='images', verbose_name='Imagem Principal'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='price',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Preço'),
        ),
    ]