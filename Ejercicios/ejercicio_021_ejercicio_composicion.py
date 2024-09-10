#Clase Item -> Nombre, número de unidades, precio unitario
#Clase Factura -> Nombre cliente, CIF, estado (emitida, pasa a cobro, rechazada, pagada) array de Items
#La clase Factura tiene una funcionalidad para generar PDF asociada a través de la composición (hacemos print incluyendo el importe)
#La clase Factura tiene una funcionalidad para generar un LOG cuando se cambie el estado asociada a través de la composición

import functools #Import para la función reduce

from enum import Enum

from ejercicio_021_generador_pdf import GeneradorPDF

class Estado(Enum):
    EMITIDA = 1
    PASA_A_COBRO = 2
    RECHAZADA = 3
    PAGADA = 4

class Item:
    def __init__(self, nombre, numero_unidades, precio_unitario) -> None:
        self.nombre = nombre
        self.numero_unidades = numero_unidades
        self.precio_unitario = precio_unitario
        self.importe = self.numero_unidades * self.precio_unitario #¿?
    
    def get_fila_factura(self):
        return f'{self.numero_unidades} de {self.nombre} a {self.precio_unitario} la unidad: {self.importe}'

    def __str__(self):
        return f'{self.numero_unidades} de {self.nombre} a {self.precio_unitario} la unidad: {self.importe}$'
    
class GeneradorLOG:
    def generar(self, texto):
        print(f'LOG: {texto}')

class Factura:
    def __init__(self, nombre_cliente, CIF, estado : Estado, items) -> None:
        self.nombre_cliente = nombre_cliente
        self.CIF = CIF
        self.__estado = estado
        self.items = items
        self.__generadorPDF = GeneradorPDF()
        self.__generadorLOG = GeneradorLOG()
    
    def set_estado(self, nuevo_estado):
        print("Cambiando de estado...")
        self.__estado = nuevo_estado
        self.__generadorLOG.generar(f'La factura {self.nombre_cliente} ha cambiado al estado {self.__estado}')

    def generarPDF(self):
        self.__generadorPDF.generar(self)
    
    def generarLOG(self):
        self.__generadorLOG.generar()

    def get_importe_con_for(self) -> int:
        importe = 0
        for item in self.items:
            importe+=item.numero_unidades * item.precio_unitario 
        return importe
    
    def get_importe_con_reduce(self) -> int:
        importe = functools.reduce(lambda total, item : total + (item.numero_unidades * item.precio_unitario), self.items, 0)
        return importe


factura = Factura("Cliente 1", "AD838433", Estado.EMITIDA, (Item("Pan",5,1),Item("Agua",10,2),Item("Leche",1,3)))
factura.generarPDF()

# factura.estado = Estado.PASA_A_COBRO #No hay detección de cambio posible
factura.set_estado(Estado.PASA_A_COBRO) #Al estar encapsulado el acceso al estado, podemos detectar los cambios