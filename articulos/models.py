from django.db import models
from distutils.command.upload import upload


class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True, verbose_name="Id de Marca")
    nombreMarca=models.CharField(max_length=50, blank=True, verbose_name="Nombre Marca")

    def __str__(self):
        return self.nombreMarca

class Producto(models.Model):
    productoId=models.AutoField(primary_key=True, verbose_name="Id Producto")
    marca= models.CharField(max_length=50, verbose_name="Marca")
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    precio=models.IntegerField(blank=True, null=True, verbose_name="Precio")

    def __str__(self):
        return self.marca
    


    

# Create your models here.
