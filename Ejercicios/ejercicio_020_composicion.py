#Crear una estructura de clases
#Clase base (Artefacto, tiene un nombre)
#3 clases derivadas de Artefacto que tienen los métodos desplazar, disparar, comunicar
#1 clase derivadas de las 3 anteriores que de lugar a la construción de una especie de carro de combate

class Desplazador:
    def desplazar(self):
        print("Desplazando...")

class Disparador:
    def disparar(self):
        print("Disparando...")

class Comunicador:
    def comunicar(self):
        print("Comunicar...")

class Artefacto:
    def __init__(self, nombre) -> None:
        print("Constructor de Artefacto")
        self.nombre = nombre

class CarroCombate(Artefacto):
    def __init__(self, nombre) -> None:
        print("Constructor de CarroCombate")
        super().__init__(nombre)
        self.__desplazador = Desplazador()
        #self.disparador = Disparador()#Se resuelve con Alternativa(1)
        self.comunicador = Comunicador()

    #Encapsulando el objeto desplazador - THE BEST
    def desplazar(self):
        self.__desplazador.desplazar()

    #Alternativa(1)
    def disparar(self):
        if (not hasattr(self, "disparador")):#Una especie de patrón singleton que sólo crea una instancia del objeto
            print("Construyendo el atributo self.disparador")
            self.__disparador = Disparador()
        self.__disparador.disparar()

carro = CarroCombate("K8000R")

#Desplazamiento
carro.desplazar() #El desplazamiento está encapsulado a través del método desplazar

#Disparo
#carro.disparador.disparar()#Se resuelve con Alternativa(1)
carro.disparar()
carro.disparar()

#Comunicación
carro.comunicador.comunicar()

