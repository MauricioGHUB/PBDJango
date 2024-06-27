from django.contrib import admin
from .models import Marca, Producto

@admin.register(Marca)
class marcaAdmin(admin.ModelAdmin):
    list_display=['idMarca','nombreMarca']
    

@admin.register(Producto)
class productoAdmin(admin.ModelAdmin):
    list_display=['productoId','nombre','imagen','precio','nombreMarca']

# Register your models here.
