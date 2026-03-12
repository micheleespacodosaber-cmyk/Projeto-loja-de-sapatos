from django.urls import path
from produto import views

app_name = 'produto'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('lista/', views.listar, name='listar'),
    path('excluir/<int:codigoProduto>/', views.excluir, name='excluir_produto'),
]