#Crear una clase en la que en el que constructor se verifiquen los tipos y los valores de los parámetros
#Clase Artefacto
#Constructor: nombre (string), coste(int), tipo (enumeracion TERRESTRE, MARINO, ESPACIAL)
#El coste no puede ser <= 0

#10:40
import enum

class Tipo(enum.Enum):
    TERRESTRE = 1
    MARINO = 2
    ESPACIAL = 3

#
# Se puede desactivar la ejecución de los assert con el argumento -O en la llamada:
# python -O ejercicio_055_ejercicio_excepciones_constructor_assert.py
#

class Artefacto():
    def __init__(self, nombre : str, coste : int, tipo : Tipo) -> None:
        #assert lanza una AssertionError cuando la expresión no es verdadera
        #Fase de validación
        assert(not isinstance(nombre, str))
        assert(type(coste)!=int)
        assert(not isinstance(tipo, Tipo))
        assert(coste<=0)
        #Código del constructor
        self.nombre = nombre
        self.coste = coste
        self.tipo = tipo

#a1 = Artefacto(3, "Tractor", Tipo.ESPACIAL)
#a1 = Artefacto(3, True, Tipo.ESPACIAL)
#a1 = Artefacto("Tractor", 3.8, Tipo.ESPACIAL)
#a1 = Artefacto("Tractor", 3, "Espacial")
a1 = Artefacto("Tractor", 1_000_000, Tipo.TERRESTRE)
print("El artefacto se ha construido correctamente")