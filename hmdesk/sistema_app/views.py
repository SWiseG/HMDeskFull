from django.shortcuts import render
from .models import *

# Create your views here.
def get_context_licenca():
    fieldLabel = 'id_licenca'
    firstLicenca = Licenca.objects.first()
    field_object = Licenca._meta.get_field(fieldLabel)
    licenca = field_object.value_from_object(firstLicenca)
    return licenca
