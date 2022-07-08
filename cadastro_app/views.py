from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Produtos

def produtos(request):
    #context - handler messages
    all_products = Produtos.objects.all
    context =  {
        'title':"Produtos",
        'all_products': all_products,
    }
    return render(request, 'Produtos/views/Produtos.html', context)