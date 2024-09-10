#Crear una estructura de clases
#Clase base (Artefacto, tiene un nombre)
#3 clases derivadas de Artefacto que tienen los métodos desplazar, disparar, comunicar
#1 clase derivadas de las 3 anteriores que de lugar a la construción de una especie de carro de combate

class Artefacto:
    def __init__(self, nombre) -> None:
        print("Constructor de Artefacto")
        self.nombre = nombre

class Desplazador(Artefacto):
    def __init__(self, nombre) -> None:
        print("Constructor de Desplazador")
        super().__init__(nombre)
    def desplazar(self):
        print("Desplazando...")

class Disparador(Artefacto):
    def __init__(self, nombre) -> None:
        print("Constructor de Disparador")
        super().__init__(nombre)
    def disparar(self):
        print("Disparando...")

class Comunicador(Artefacto):
    def __init__(self, nombre) -> None:
        print("Constructor de Comunicador")
        super().__init__(nombre)
    def comunicar(self):
        print("Comunicar...")

class CarroCombate(Desplazador, Disparador, Comunicador):
    def __init__(self, nombre) -> None:
        print("Constructor de CarroCombate")
        super().__init__(nombre)

#ATENCIÓN: si los constructores de las clases base de CarroCombate no coinciden en número, tipo y semántica, los constructores no tiene solución lógica
carro = CarroCombate("K8000R")
print(carro.nombre)

carro.comunicar()
carro.desplazar()
carro.disparar()

