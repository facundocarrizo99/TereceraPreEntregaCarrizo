from django import forms
from .models import Cliente, Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class BusquedaClienteForm():
    nombre = forms.CharField(min_length=3, max_length=40)

class BusquedaProductoForm():
    nombre = forms.CharField(min_length=3, max_length=40)