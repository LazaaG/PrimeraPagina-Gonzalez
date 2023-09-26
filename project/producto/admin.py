from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Categoria)
admin.site.register(models.Producto)