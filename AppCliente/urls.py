from django.urls import path

from AppCliente import views
from AppCliente.views import *

urlpatterns = [
    path('cliente/', views.cliente, name="cliente"),
    path('cliente/new', views.crearCliente, name="AppTercerEntrega"),
    path('producto/new', views.crearProducto, name="AppTercerEntrega"),
]