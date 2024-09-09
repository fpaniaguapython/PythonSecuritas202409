#Crear una clase Factura
#--nombre cliente, importe, anyo_emision

#Creamos una lista con 5 instancias de factura (al menos dos comparten nombre nombre y son <2023)

#Mediante comprensión de listas, crear una nueva lista con las facturas
#que sean anteriores a 2023 y que esté ordenada por nombre de cliente
#y si los nombres son iguales, por importe de mayor a menor

class Factura:
    def __init__(self, nombre, importe : int, anyo_emision) -> None:
        self.nombre = nombre
        self.importe = importe
        self.anyo_emision = anyo_emision
    
    def __lt__(self, other):
        return self.nombre < other.nombre if self.nombre!=other.nombre else self.importe > other.importe 

    def __repr__(self) -> str:
        return self.nombre + ":" + str(self.importe) + ":" + str(self.anyo_emision)

f1 = Factura("C1",8_000,2021)
f2 = Factura("C2",24_000,2021)
f3 = Factura("C2",10_000,2021)
f4 = Factura("C3",15_000,2024)
f5 = Factura("C4",20_000,2023)

facturas = [f1, f2, f3, f4, f5]

facturas_antiguas = [factura for factura in facturas if factura.anyo_emision<2023]
facturas_antiguas.sort()

print(facturas_antiguas)

