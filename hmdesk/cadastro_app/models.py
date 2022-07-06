
from django.db import models
from framework.models import ModelConsts
from datetime import datetime
import uuid

# Create your models here.

class Produtos(models.Model):
    id_produto = models.UUIDField(max_length= ModelConsts.KEY_LENGTH, primary_key=True, default=uuid.uuid4, editable=False, blank=False, name='ID_PRODUTO')
    codigo = models.CharField(max_length= ModelConsts.CODIGO_LENGTH, editable=False, auto_created=True, name='CODIGO')
    descricao = models.CharField(max_length= ModelConsts.DESCRICAO_LENGTH, name= 'DESCRICAO')
    valor_unit = models.IntegerField(name='VALOR')
    usuario_inclusao = models.CharField(max_length=50, name='USUARIO_INCLUSAO')
    data_inclusao = models.DateTimeField(default=datetime.now, blank=True, name='DATA_INCLUSAO')
    usuario_alteracao = models.CharField(max_length=50, name='USUARIO_ALTERAÇAO')
    data_alteracao = models.DateTimeField(default=datetime.now, blank=True,name='DATA_ALTERAÇAO')

    