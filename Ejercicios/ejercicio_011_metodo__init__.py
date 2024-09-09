#Uso de super() y de __init__

class Vehiculo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Terrestre(Vehiculo):
    def __init__(self, nombre, numero_ruedas) -> None:
        super().__init__(nombre) #Llamada explícita a un método 'mágico' o especial
        self.numero_ruedas = numero_ruedas

t = Terrestre("Automóvil", 4)
print(t.nombre)