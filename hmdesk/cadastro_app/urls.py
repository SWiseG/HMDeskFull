from django.urls import path
from .views import *

urlpatterns = [
    # Categoria
    # Fornecedor
    # Produto
    path('Produtos', produto_list, name='produto'),
    path('Produtos/Novo', produto_new, name='produto_new'),
    path('Produtos/Editar/<id_produto>', produto_edit, name='produto_edit'),
    path('Produtos/Excluir/<id_produto>', produto_delete, name='produto_delete'),
    path('Produtos/Detalhes/<id_produto>', produto_detail, name='produto_detail'),
]
