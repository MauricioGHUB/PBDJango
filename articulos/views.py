
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Producto
from .forms import  ProductoForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def crear(request):
    return render(request,'crud/crear.html')


def producto_detalle(request):
    return render(request,'crud/detalle.html')
# CRUD para producto 
def producto_lista(request):
    productos = Producto.objects.all()
    context={

        'productos':productos
    }
    return render(request, 'articulos.html',context)


def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_lista')
    else:
        form = ProductoForm()
    return render(request, 'crud/crear.html', {'form': form})
    


def producto_editar(request, id):
    producto = Producto.objects.get(productoId=id)
    datos= {
        'form':ProductoForm(instance=producto)
    }   
    if request.method == "POST":
        form = ProductoForm(data=request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('articulos.html')
        
    return render(request, "crud/modificar.html", datos)


def producto_borrar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('articulos.html')
    return render(request, 'articulos.html', {'producto': producto})

def MostrarGPS(request):
    return render(request,'Example/artGPS.html')

def MostrarVolante(request):
    return render(request,'Example/artVOLANTE.html')

def MostrarCadena(request):
    return render(request,'Example/artCADENA.html')

def MostrarCasco(request):
    return render(request,'Example/artCasco.html')

@login_required
def MostrarProductos(request):
    return render(request,'productosEST.html')




