from django.urls import path
from .views import *

urlpatterns = [
    # Pessoa
    path('Pessoas', pessoa_list, name='pessoa'),
    path('Pessoas/Novo', pessoa_new, name='pessoa_new'),
    path('Pessoas/Editar/<id_pessoa>', pessoa_edit, name='pessoa_edit'),
    path('Pessoas/Excluir/<id_pessoa>', pessoa_delete, name='pessoa_delete'),
    path('Pessoas/Detalhes/<id_pessoa>', pessoa_detail, name='pessoa_detail'),
]
