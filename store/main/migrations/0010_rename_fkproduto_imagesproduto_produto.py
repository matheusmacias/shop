# Generated by Django 4.1.4 on 2022-12-25 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_imagesproduto_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagesproduto',
            old_name='fkProduto',
            new_name='produto',
        ),
    ]