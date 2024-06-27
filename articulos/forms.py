# forms.py
from django import forms
from .models import Marca, Producto

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombreMarca']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['productoId','nombre','imagen','precio','nombreMarca']
