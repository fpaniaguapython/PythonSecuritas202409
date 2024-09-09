#Crear una clase Factura con el atributo de clase IVA (21)
#En el constructor se recibe una tupla de importes
#Crear un método calcular_importe_total que devuelva la suma de importes + el IVA correspondiente

class Factura:
    IVA = 21 
    def __init__(self, importes) -> None:
        self.importes = importes

    def calcular_importe_total(self):
        subtotal = sum(self.importes)
        total = subtotal + (subtotal * Factura.IVA/100) #Haciendo uso de la variable de clase
        return total
    
f1 = Factura(importes=(10,50,40))
total = f1.calcular_importe_total()
print(total)

print(f1.__dict__) #{'importes': (10, 50, 40)}
print(Factura.__dict__) #Además de otras cosas, muestra 'IVA': 21,