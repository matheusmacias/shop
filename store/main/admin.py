from django.contrib import admin

from .models import Produto, ImagesProduto, CoresProduto, TamanhoProduto

admin.site.register(Produto)
admin.site.register(ImagesProduto)
admin.site.register(CoresProduto)
admin.site.register(TamanhoProduto)
