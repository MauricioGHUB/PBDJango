class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito
    
    def agregar(self, producto):
        if producto_id not in self.carrito.keys:
            self.carrito[producto_id] = {
                "producto_id": producto.productoId,
                "nombre": producto.nombre,
                "nombreMarca": producto.nombreMarca,
                "precio": str(producto.precio),  # Convertir a str para serialización
                "cantidad": 1,
                "total": producto.precio,
                "imagen": producto.imagen.url if producto.imagen else None  # Agregar imagen si existe
            }
        else:
            for key, value in self.carrito.items():
                if key == producto.productoid:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = producto.precio
                    value["total"]= value["total"] + producto.precio
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
        for key, value in self.carrito.items():
            if key == producto_id:
                value["cantidad"] -= 1
                value["total"] = float(value["total"]) - producto.precio
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
