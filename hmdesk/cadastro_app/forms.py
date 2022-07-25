from django import forms
from .models import *

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao','valor_unitario_compra','valor_unitario_venda']