from django.shortcuts import render
from AppCliente.models import Cliente, Producto, SaveProducto, SaveCliente
from django import forms


# Create your views here.
def cliente(request):
    return render(request, "clientes.html")

def crearCliente(request):
    if request.method == "POST":
        saveCliente = SaveCliente(request.POST)
    else:
        saveCliente = Cliente()
    return render(request, "saveCliente.html", {"form":saveCliente})

def crearProducto(request):
    if request.method == "POST":
        form = SaveProducto(request.POST)
        if form.is_valid():
            name = form.cleaned_data["nombre"]
            price = form.cleaned_data["precio"]
            quantity = form.cleaned_data["cantidad"]
            t = Cliente(nombre=name, precio=price, cantidad=quantity)
            t.save()
    else:
        saveProducto = Producto()
    return render(request, "saveProducto.html",  {"form":saveProducto})
