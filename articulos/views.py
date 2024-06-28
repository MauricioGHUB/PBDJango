
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
    marca = Marca.objects.all()

    producto.nombre = request.POST['nombre']
    producto.precio = request.POST['precio']
    producto.nombreMarca = request.POST['nombre marca']

    if 'imagen' in request.FILES:
        producto.imagen = request.FILES['imagen']
    producto.save()

    context = {

        'producto':producto,
        'Marca':marca
    }
    return render(request, "crud/modificar.html", context)



def producto_borrar(request, pk):
    producto = get_object_or_404(Producto, productoId =pk)

    context = {
        'producto': producto
    }
    return render(request, 'articulos.html',context)

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




