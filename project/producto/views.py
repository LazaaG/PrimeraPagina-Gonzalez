from django.shortcuts import render, redirect

from . import models, forms


def index(request):
    productos = models.Producto.objects.all()

    return render(request, "producto/index.html", {"productos": productos})

def crear_producto(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    else:
        form = forms.ProductoForm()
    return render(request, "producto/crear_producto.html", {"form": form})

def crear_categoria(request):
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    else:
        form = forms.CategoriaForm()
    return render(request, "producto/crear_categoria.html", {"form": form})

def crear_stock(request):
    if request.method == "POST":
        form = forms.StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    else:
        form = forms.StockForm()
    return render(request, "producto/crear_stock.html", {"form": form})