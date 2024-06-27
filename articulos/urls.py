from django.urls import path
from .views import producto_lista, producto_nuevo, producto_editar, producto_borrar, producto_detalle

urlpatterns = [
    path('productos', producto_lista, name='producto_lista'),  # Lista de productos
    path('productos/nuevo', producto_nuevo, name='producto_nuevo'),  # Crear nuevo producto
    path('productos/editar/', producto_editar, name='producto_editar'),  # Editar producto
    path('productos/borrar/', producto_borrar, name='producto_borrar'),  # Borrar producto
    path('productos/detalle/<int:id>/',producto_detalle, name='producto_detalle')
]
