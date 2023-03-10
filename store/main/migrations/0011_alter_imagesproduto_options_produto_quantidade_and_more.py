# Generated by Django 4.1.4 on 2023-01-04 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_fkproduto_imagesproduto_produto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesproduto',
            options={'verbose_name_plural': 'ImagesProduto'},
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade'),
        ),
        migrations.CreateModel(
            name='TamanhoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=100, verbose_name='Tamanho')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.produto')),
            ],
            options={
                'verbose_name_plural': 'TamanhoProduto',
            },
        ),
        migrations.CreateModel(
            name='CoresProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=40, verbose_name='Cor')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.produto')),
            ],
            options={
                'verbose_name_plural': 'coresProduto',
            },
        ),
    ]
