from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from multiprocessing import context
from .models import *
from .forms import *


# PRODUTO
def produto_list(request):
    #context - handler messages
    all_products = Produto.objects.all
    context =  {
        'title':"Produtos",
        'all_products': all_products,
    }
    return render(request, 'Produtos/views/List.html', context)

def produto_new(request):
    #context - handler messages
    if request.method == "POST":
        form = ProdutoForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('produto')
    else:
        context =  {
            'title':"Produtos",
        }
        return render(request, 'Produtos/views/New.html', context)  

def produto_edit(request, id_produto):
    #context - handler messages
    if request.method == "POST":
        produto = Produto.objects.get(pk=id_produto)
        form = ProdutoForm(request.POST or None, instance=produto)
        if form.is_valid():
            form.save()
        return redirect('produto')
    else:
        produto = Produto.objects.get(pk=id_produto)
        context =  {
            'title':"Produtos",
            'produto': produto,
        }
    return render(request, 'Produtos/views/Edit.html', context)

def produto_delete(request, id_produto):
    #context - handler messages
    produto = Produto.objects.get(pk=id_produto)
    produto.delete()
    return redirect('produto')

def produto_detail(request, id_produto):
    #context - handler messages
    produto = Produto.objects.get(pk=id_produto)
    context =  {
        'title':"Produtos",
        'produto': produto,
    }
    return render(request, 'Produtos/views/Detail.html', context)