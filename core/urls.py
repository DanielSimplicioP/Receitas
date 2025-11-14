# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # (US 2) Lista - / (página inicial)
    path('', views.listar_receitas, name='listar_receitas'),

    # (US 1) Cadastro - /cadastrar/
    path('cadastrar/', views.cadastrar_receita, name='cadastrar_receita'),

    # (US 3) Detalhe - /receita/1/ (o 1 é um exemplo de ID)
    path('receita/<int:pk>/', views.detalhe_receita, name='detalhe_receita'),

    # (US 4) Excluir - /excluir/1/
    path('excluir/<int:pk>/', views.excluir_receita, name='excluir_receita'),
]