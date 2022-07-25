from django import forms
from .models import *

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome','cnpjcpf','email','telefone','rede_social']