from django.shortcuts import render
from .models import Produto
from django.shortcuts import redirect
from django.http import Http404


def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos,
    }
    return render(request, 'home/home.html', context)


def produto(request, url_produto):
    # transformar url em array
    transformArrayUrl = url_produto.split('-')
    # Try para verificar se o id é um numero, caso contrario retonará pagina não encontrada
    try:
        # pegar ultimo elemento do array (id)
        id_produto = int(transformArrayUrl[-1])
    except ValueError:
        raise Http404("Página não encontrada")

    # pegar o tamanho do array
    length_url = len(transformArrayUrl) - 1
    # remover o ultimo elemento do array (id)
    transformArrayUrl.pop(length_url)
    # transformar array em uma String
    nome_produto = ' '.join(transformArrayUrl)

    try:
        produto = Produto.objects.get(
            name=nome_produto, id=id_produto)
    except:
        raise Http404("Página não encontrada")

    context = {
        'produto': produto,
    }
    return render(request, 'home/produto.html', context)
