from django.db import models
from django import forms


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    carrito = []

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class SaveCliente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()


class SaveProducto(forms.Form):
    nombre = forms.CharField(max_length=40)
    precio = forms.FloatField()
    cantidad = forms.IntegerField()