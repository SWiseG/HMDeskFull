from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    #context - handler messages
    context =  {
        'title':"Menu",
    }
    return render(request, 'Menu/views/Menu.html', context)
