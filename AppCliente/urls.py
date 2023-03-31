from django.urls import path

from AppCliente import views
from AppCliente.views import *

urlpatterns = [
    path('', homeScreen, name="HomeScreen"),
    path('cliente/', cliente, name="Clientes"),
    path('producto/', productos, name="Productos"),
    path('cliente/new', crearCliente, name="AppTercerCrearCliente"),
    path('producto/new', crearProducto, name="AppTercerCrearProducto"),
]