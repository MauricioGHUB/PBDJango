from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import producto_lista, producto_nuevo, producto_editar, producto_borrar,producto_detalle, MostrarGPS, MostrarVolante, MostrarCadena, MostrarGPS, MostrarVolante, MostrarCasco, MostrarProductos, Inicio
from . import views
urlpatterns = [
    path('',Inicio, name='inicio'),  # Ruta de inicio
    path('productos', producto_lista, name='producto_lista'),  # Lista de productos
    path('productos/nuevo', producto_nuevo, name='producto_nuevo'),  # Crear nuevo producto
    path('productos/editar/<int:id>/', producto_editar, name='producto_editar'),  # Editar producto
    path('productos/borrar/<int:pk>/', views.producto_borrar, name='producto_borrar'),  # Borrar producto
    path('productos/detalle/<int:id>/',producto_detalle, name='producto_detalle'),
    path('gps/',MostrarGPS,name='MostrarGPS'),
    path('volante/',MostrarVolante,name='MostrarVolante'),
    path('cadena/',MostrarCadena,name='MostrarCadena'),
    path('casco/',MostrarCasco,name='MostrarCasco'),
    path('producto/',MostrarProductos,name='MostrarProducto'),
]
