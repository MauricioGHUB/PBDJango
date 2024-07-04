from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
<<<<<<< HEAD
from django.http import HttpResponseForbidden
=======
>>>>>>> 2a299d840889c4f13049a2bc2ab5b8be73f5ead9
from .models import Producto, Marca, CarritoProducto
from .forms import  ProductoForm
from django.contrib.auth.decorators import login_required
from .carrito import Carrito
from django.http import JsonResponse
from .serializers import MarcaSerializer
<<<<<<< HEAD
from functools import wraps
=======
>>>>>>> 2a299d840889c4f13049a2bc2ab5b8be73f5ead9

# Create your views here.
def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

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
        form = ProductoForm(request.POST, request.FILES)
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



def tienda(request):
    producto = Producto.objects.all()
    context = {
        'producto': producto  # Contexto como un diccionario
    }
    return render(request, 'crud/tienda.html',context)


def agregar_producto(request, id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, pk=id)
    carrito.agregar(producto=producto)

    # Acceder explícitamente a los campos relacionados para evitar DeferredAttribute
    producto_data = {
        'id': producto.productoId,
        'nombre': producto.nombre,
        'precio': producto.precio,
        'marca': {
            'id': Marca.idMarca,
            'nombre': Marca.nombreMarca,
            # Agregar más campos según sea necesario
        }
        # Agregar más campos del producto según sea necesario
    }

    return JsonResponse({'producto': producto_data})

def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, productoId=producto_id)
    carrito = Carrito(request)
    carrito.eliminar(producto)
    return redirect('carrito')

def restar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, productoId=producto_id)
    carrito = Carrito(request)
    carrito.restar(producto)
    return redirect('carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito')

def ver_carrito(request):
    carrito = Carrito(request)
    return render(request, 'carrito.html', {'carrito': Carrito.carrito})

def generarBoleta(request):
    precio_total =0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + (int(value['precio']))(int(value['cantidad']))
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
        productoId = Producto.objects.get(productoId= value['Id Producto'])
        cant = value['cantidad']
        subtotal = cantint(value['precio'])
        detalle = DetalleBoleta(id_boleta= boleta, id_producto = productoId, cantidad = cant,subtotal= subtotal)
        detalle.save()
        productos.append(detalle)

    datos = {
        'productos':productos,
        'fecha': boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request,'carrito/detallecarrito.html',datos)


def lista_productos(request):
    productos = Producto.objects.all()
<<<<<<< HEAD
    return render(request, 'productosEST.html', {'productos': productos})
=======
    return render(request, 'productosEST.html', {'productos': productos})


>>>>>>> 2a299d840889c4f13049a2bc2ab5b8be73f5ead9
