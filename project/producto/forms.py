from django import forms

from . import models


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre", "descripcion", "precio", "categoria", "stock"]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ["nombre"]

class StockForm(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ["stock"]