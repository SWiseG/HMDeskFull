from django.urls import path
from cadastro_app import views

urlpatterns = [
    path('Produtos', views.produtos, name='produtos'),
]
