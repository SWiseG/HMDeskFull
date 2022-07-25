from django.db import models
from sistema_app.models import Licenca
from sistema_app.views import get_context_licenca
from datetime import *
import uuid

# Create your models here.
now = datetime.now()
class Pessoa(models.Model):
    id_pessoa = models.UUIDField(primary_key=True, max_length=50, default=uuid.uuid4, editable=False)
    id_licenca = models.ForeignKey(Licenca, default=get_context_licenca(),on_delete=models.CASCADE, db_column='id_licenca')
    nome = models.CharField(max_length=255)
    cnpjcpf = models.CharField(max_length=14, blank=True, null=True)
    data_inclusao = models.DateTimeField(default=now,blank=True, null=True)  # This field type is a guess.
    usuario_inclusao = models.CharField(max_length=50, blank=True, null=True)
    data_alteracao = models.DateTimeField(default=now,blank=True, null=True)  # This field type is a guess.
    usuario_alteracao = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    rede_social = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cad_pessoa'

    