from django.shortcuts import render
from AppCliente.models import Cliente, Producto

# Create your views here.
def cliente(request):
    return render(request, "clientes.html")

def crearCliente(request):
    if request.method == "POST":
        saveCliente = Cliente(request.POST)
    else:
        saveCliente = Cliente()
    return render(request, "saveCliente.html", {"form":saveCliente})

def crearProducto(request):
    if request.method == "POST":
        saveProducto = Producto(request.POST)
    else:
        saveProducto = Producto()
    return render(request, "saveProducto.html",  {"form":saveProducto})
