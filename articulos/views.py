
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Producto,Marca
from .forms import  ProductoForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def crear(request):
    return render(request,'crud/crear.html')


def producto_detalle(request, id):
    producto = get_object_or_404(Producto, productoId=id)
    context = {
        'productos': [producto]
    }
    return render(request, 'crud/detalle.html', context)

# CRUD para producto 

@login_required
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
    producto = get_object_or_404(Producto, productoId=id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige a la página principal o lista de productos
    else:
        form = ProductoForm(instance=producto)

    context = {
        'form': form
    }
    return render(request, 'crud/modificar.html', context)



def producto_borrar(request, pk):
    producto = get_object_or_404(Producto, productoId=pk)
    producto.delete()
    return redirect('Inicio') 

def MostrarGPS(request):
    return render(request,'Example/artGPS.html')

def MostrarVolante(request):
    return render(request,'Example/artVOLANTE.html')

def MostrarCadena(request):
    return render(request,'Example/artCADENA.html')

def MostrarCasco(request):
    return render(request,'Example/artCasco.html')

def MostrarProductos(request):
    return render(request,'productosEST.html')

def Inicio(request):
    return render(request,'inicio/index.html')



