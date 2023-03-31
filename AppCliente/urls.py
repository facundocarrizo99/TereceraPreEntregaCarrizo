from django.urls import path

from AppCliente import views
from AppCliente.views import *

urlpatterns = [
    path('', cliente, name="HomeScreen"),
    path('cliente/new', crearCliente, name="AppTercerCrearCliente"),
    path('producto/new', crearProducto, name="AppTercerCrearProducto"),
]