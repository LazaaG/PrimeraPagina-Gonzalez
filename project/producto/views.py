from django.shortcuts import render, redirect

from . import models, forms


def index(request):
    productos = models.Producto.objects.all()

    return render(request, "producto/index.html", {"productos": productos})

def crear(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    else:
        form = forms.ProductoForm()
    return render(request, "producto/crear.html", {"form": form})