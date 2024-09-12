class Producto:
    def __init__(self, nombre, precio_unitario):
        self.nombre = nombre
        self.precio_unitario = precio_unitario

class Cesta:
    __tiempo_caducidad = 10
    
    def __init__(self) -> None:
        self.productos = []

    def add_producto(self, producto : Producto):
        self.productos.append(producto)

    @classmethod
    def modificar_caducidad(cls, nueva_caducidad):
        cls.__tiempo_caducidad = nueva_caducidad

    @staticmethod
    def get_cesta(tupla_items):
        cesta =  Cesta()
        for item in tupla_items:
            cesta.add_producto(Producto(item[0],item[1]))
        return cesta


cesta1 = Cesta()

cesta2 = Cesta.get_cesta((("Pan",1),("Leche",2)))
