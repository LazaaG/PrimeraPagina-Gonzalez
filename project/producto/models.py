from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20, validators=[
            MinLengthValidator(limit_value=3, 
                               message="La categoria debe tener al menos 3 letras.")
        ])

    def __str__(self) -> str:
        return self.nombre

class Stock(models.Model):
    stock = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.stock

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=25, blank=True)
    precio = models.FloatField(max_length=6)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nombre