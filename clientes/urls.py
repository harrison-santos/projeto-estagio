from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.clientesListar, name="clientesListar"),
    path('cadastrar', views.clientesCadastrar, name="clientesCadastrar"),
    path('<int:cliente_id>/deletar', views.clientesDeletar, name="clientesDeletar"),
    path('<int:cliente_id>/editar', views.clientesEditar, name="clientesEditar"),

    path('<int:cliente_id>/enderecos', views.enderecosListar, name="enderecosListar"),
    path('<int:cliente_id>/enderecos/cadastrar', views.enderecosCadastrar, name="enderecosCadastrar"),
    url('(?P<cliente_id>[0-9]+)/enderecos/(?P<endereco_id>[0-9]+)/editar', views.enderecosEditar, name="enderecosEditar"),
    url('(?P<cliente_id>[0-9]+)/enderecos/(?P<endereco_id>[0-9]+)/deletar', views.enderecosDeletar, name="enderecosDeletar")


]