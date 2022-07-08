from django.urls import path
from menu_app import views

urlpatterns = [
    path('Menu', views.menu, name='menu'),

]
