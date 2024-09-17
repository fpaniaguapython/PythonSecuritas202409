lista = [3,8,-1,5,2]
print(max(lista)) #8

lista = ['primavera','verano','otoño','invierno']
print(max(lista))#verano

lista = [(3,1),(8,15),(-1,2000),(5,-8),(2,'dos')]
print(max(lista)) #(8, 15)

#lista = [(3,1),(8,15),(-1,2000),("cinco",-8),(2,2)]
#print(max(lista)) #TypeError

class Factura:
    def __init__(self, numero, importe) -> None:
        self.numero = numero
        self.importe = importe

    def __gt__(self, other):
        return self.importe > other.importe
    
    def __str__(self):
        return str(self.numero)

f1 = Factura(1000,5000)
f2 = Factura(1005,800)
f3 = Factura(1002,5500)

facturas = (f1,f2,f3)

print("Número de factura:", max(facturas))

