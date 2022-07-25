from django.urls import path
from menu_app import views

urlpatterns = [
    path('', views.menu, name='menu'),

]
