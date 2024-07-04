import json
from django.core.serializers.json import DjangoJSONEncoder

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito
    
 
    def agregar(self, producto):
        if str(producto.productoId) not in self.carrito:
            self.carrito[str(producto.productoId)] = {
                "producto_id": producto.productoId,
                "nombre": producto.nombre,
                "Marca": producto.nombreMarca,
                "precio": str(producto.precio),
                'cantidad': 1,
                "imagen": producto.imagen.url,
                "total": producto.precio
            }
        else:
            for key, value in self.carrito.items():
                if key == str(producto.productoId):
                    value["cantidad"] += 1
                    value["total"] = str(int(value["total"]) + producto.precio)
                    break
        self.guardar_carrito()



    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.productoId)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar_carrito()
    
    def restar(self, producto):
        producto_id = str(producto.productoId)
        if producto_id in self.carrito:
            self.carrito[producto_id]["cantidad"] -= 1
            self.carrito[producto_id]["total"] -= producto.precio
            if self.carrito[producto_id]["cantidad"] < 1:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
