from django.urls import path
from fabricante import views

app_name = 'fabricante'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('lista/', views.listar, name='lista'),
]