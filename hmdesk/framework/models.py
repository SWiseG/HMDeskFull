import sys
from django.db import models

class ModelConsts(models.Model):

    KEY_LENGTH = 50;
    DOUBLE_KEY_LENGTH = 100;
    NOME_LENGTH = 100;
    DESCRICAO_LENGTH = 200;
    DESCRICAO_DUPLA_LENGTH = 400;
    SYNC_LENGTH = 250;
    TRADUCAO_LENGTH = 2000;
    MAX_STR_LENGTH = 4000;
    CODIGO_LENGTH = 50;
    FONE_LENGTH = 50;
    BOOL_LENGTH = 1;
    STATUS_LENGTH = 1;
    TIPO_LENGTH = 2;
    FLAGS_LENGTH = 12;
    CULTURE_LENGTH = 5;
    ANO_MES_LENGTH = 7;

    BOOL_TRUE = "S";
    BOOL_FALSE = "N";