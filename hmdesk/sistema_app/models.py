from django.db import models
from datetime import *
import uuid
# Create your models here.
    
class Licenca(models.Model):
    id_licenca = models.BigIntegerField(primary_key=True, default=1, editable=False)
    descricao = models.CharField(max_length=200)
    dominio = models.CharField(max_length=2000, blank=True, null=True)
    tenant = models.UUIDField(max_length=50, default=uuid.uuid4, editable=False, blank=True, null=True)
    ativo = models.CharField(max_length=1,default="S")

    class Meta:
        managed = False
        db_table = 'sis_licenca'
        unique_together = (('id_licenca', 'tenant'),)

class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, max_length=50, default=uuid.uuid4, editable=False)
    id_licenca = models.BigIntegerField()
    nome = models.CharField(max_length=100)
    usuario_ad = models.CharField(max_length=50, blank=True, null=True)
    senha = models.CharField(max_length=400, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    data_expiracao = models.TextField(blank=True, null=True)  # This field type is a guess.
    numero_tentativas = models.BigIntegerField()
    historico_senhas = models.CharField(max_length=255, blank=True, null=True)
    ativo = models.CharField(max_length=1)
    data_inclusao = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuario_inclusao = models.CharField(max_length=50, blank=True, null=True)
    data_alteracao = models.TextField(blank=True, null=True)  # This field type is a guess.
    usuario_alteracao = models.CharField(max_length=50, blank=True, null=True)
    provider = models.CharField(max_length=200, blank=True, null=True)
    bloqueado = models.CharField(max_length=1)

    class Meta:
        managed = True
        db_table = 'sis_usuario'