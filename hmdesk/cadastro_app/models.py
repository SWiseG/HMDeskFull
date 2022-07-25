from django.db import models
from sistema_app.models import Licenca
from datetime import *
import uuid

# Create your models here.

class Produto(models.Model):
    id_produto = models.UUIDField(primary_key=True, max_length=50, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    valor_unitario_compra = models.DecimalField(decimal_places=2,default=0,max_digits=11)
    valor_unitario_venda = models.DecimalField(decimal_places=2,default=0,max_digits=11)
    data_inclusao = models.DateTimeField(default=datetime.now(),blank=True, null=True)  # This field type is a guess.
    usuario_inclusao = models.CharField(max_length=50, blank=True, null=True)
    data_alteracao = models.DateTimeField(default=datetime.now(),blank=True, null=True)  # This field type is a guess.
    usuario_alteracao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cad_produto'

    