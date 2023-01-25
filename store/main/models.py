from django.db import models


class Produto(models.Model):
    imagemain = models.ImageField(
        'Imagem Principal', upload_to='images', default='')
    name = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=3000, default='')
    price = models.FloatField('Preço', default=0)
    quantidade = models.PositiveIntegerField('Quantidade', default=0)

    def __str__(self):
        return self.name


class ImagesProduto(models.Model):
    image = models.ImageField(
        'Imagem', upload_to='images', default='')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.produto)

    class Meta:
        verbose_name_plural = "ImagesProduto"


class CoresProduto(models.Model):
    cor = models.CharField('Cor', max_length=40)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cor)

    class Meta:
        verbose_name_plural = "coresProduto"


class TamanhoProduto(models.Model):
    tamanho = models.CharField('Tamanho', max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tamanho)

    class Meta:
        verbose_name_plural = "TamanhoProduto"
