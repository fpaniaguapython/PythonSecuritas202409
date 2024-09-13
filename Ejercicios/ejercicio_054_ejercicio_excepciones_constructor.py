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

class Artefacto():
    def __init__(self, nombre : str, coste : int, tipo : Tipo) -> None:
        if (not isinstance(nombre, str)):
            raise TypeError("El nombre tiene que ser str")
        if (type(coste)!=int):#Para que no se cuele 'bool', ya que es clase derivada de 'int'
            raise TypeError("El coste tiene que ser int")
        if (not isinstance(tipo, Tipo)):
            raise TypeError("El tipo tiene que ser Tipo")
        if (coste<=0):
            raise ValueError("El coste debe ser positivo")
        self.nombre = nombre
        self.coste = coste
        self.tipo = tipo

try:
    #a1 = Artefacto(3, "Tractor", Tipo.ESPACIAL)
    #a1 = Artefacto(3, True, Tipo.ESPACIAL)
    #a1 = Artefacto("Tractor", 3.8, Tipo.ESPACIAL)
    #a1 = Artefacto("Tractor", 3, "Espacial")
    a1 = Artefacto("Tractor", 1_000_000, Tipo.TERRESTRE)
    print("El artefacto se ha construido correctamente")
except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)
finally:
    print("Fin del intento de construcción del artefacto")

