from django.shortcuts import render
from AppCliente.models import Cliente, Producto
from .forms import ClienteForm, ProductoForm, BusquedaClienteForm, BusquedaProductoForm


# Create your views here.
def homeScreen(request):
    return render(request, "base.html")
def cliente(request):
    all_clientes = Cliente.objects.all()
    context = {
        "clientes": all_clientes,
        "form_busqueda": BusquedaClienteForm(),
    }
    return render(request, "clientes.html", context=context)

def productos(request):
    all_productos = Producto.objects.all()
    context = {
        "productos": all_productos,
        "form_busqueda": BusquedaProductoForm(),
    }
    return render(request, "productos.html", context=context)

def crearCliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["nombre"]
            surname = form.cleaned_data["apellido"]
            mail = form.cleaned_data["email"]
            t = Cliente(nombre=name, apellido=surname, email=mail)
            t.save()
    context = {
        "form": ClienteForm()
    }
    return render(request, "saveCliente.html", context=context)

def crearProducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["nombre"]
            price = form.cleaned_data["precio"]
            quantity = form.cleaned_data["cantidad"]
            t = Producto(nombre=name, precio=price, cantidad=quantity)
            t.save()
    context = {
        "form": ProductoForm()
    }
    return render(request, "saveProducto.html", context=context)
