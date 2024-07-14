from django.urls import path
from .views import producto_lista, producto_nuevo, producto_editar, producto_borrar, producto_detalle, generarBoleta,tienda,ver_carrito, compras_cliente, ver_compras_todos_clientes
from . import views 

urlpatterns = [
    path('tienda/', tienda, name='tienda'),
    path('productos/nuevo', producto_nuevo, name='producto_nuevo'),
    path('productos/editar/<int:id>/', producto_editar, name='producto_editar'),
    path('productos/borrar/<int:pk>/', views.producto_borrar, name='producto_borrar'),
    path('productos/detalle/<int:id>/',producto_detalle, name='producto_detalle'),
    path('carrito/', ver_carrito, name='carrito'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
    path('generarBoleta/', views.generarBoleta, name='generarBoleta'),
    path('agregar_producto/<id>/', views.agregar_producto, name='agregar_producto'),
    path('restar_producto/<id>/', views.restar_del_carrito, name='restar_producto'),
    path('productos/', producto_lista, name='lista_productos'),
    path('compras/', compras_cliente, name='compras_cliente'),
    path('admin/compras/', ver_compras_todos_clientes, name='compras_todos_clientes'),
]
