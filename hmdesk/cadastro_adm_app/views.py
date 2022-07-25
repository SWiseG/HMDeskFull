from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from multiprocessing import context
from .models import *
from .forms import *


# PRODUTO
def pessoa_list(request):
    #context - handler messages
    all_people = Pessoa.objects.all
    context =  {
        'title':"Pessoas",
        'all_people': all_people,
    }
    return render(request, 'Pessoas/views/List.html', context)

def pessoa_new(request):
    #context - handler messages
    if request.method == "POST":
        form = PessoaForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('pessoa')
    else:
        context =  {
            'title':"Pessoas",
        }
        return render(request, 'Pessoas/views/New.html', context)  

def pessoa_edit(request, id_pessoa):
    #context - handler messages
    if request.method == "POST":
        pessoa = Pessoa.objects.get(pk=id_pessoa)
        form = PessoaForm(request.POST or None, instance=pessoa)
        if form.is_valid():
            form.save()
        return redirect('pessoa')
    else:
        pessoa = Pessoa.objects.get(pk=id_pessoa)
        context =  {
            'title':"Produtos",
            'pessoa': pessoa,
        }
    return render(request, 'Pessoas/views/Edit.html', context)

def pessoa_delete(request, id_pessoa):
    #context - handler messages
    pessoa = Pessoa.objects.get(pk=id_pessoa)
    pessoa.delete()
    return redirect('pessoa')

def pessoa_detail(request, id_pessoa):
    #context - handler messages
    pessoa = Pessoa.objects.get(pk=id_pessoa)
    context =  {
        'title':"Pessoas",
        'pessoa': pessoa,
    }
    return render(request, 'Pessoas/views/Detail.html', context)