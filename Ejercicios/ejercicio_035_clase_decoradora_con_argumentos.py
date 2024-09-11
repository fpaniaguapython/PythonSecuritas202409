from enum import Enum

class Modo(Enum):
    CLARO = 'Claro'
    OSCURO = 'Oscuro'

class DecoradorConArgumentos:
    def __init__(self, modo) -> None: #Recibimos en el constructor los argumentos del decorador
        self.modo = modo

    def __call__(self, funcion_a_decorar): #Recibimos la función a decorar
        def wrapper_interno(*args, **kwargs): #Recibimos los argumentos de la función a decorar
            if (self.modo==Modo.CLARO):
                print("Estoy en modo claro")
            elif (self.modo==Modo.OSCURO):
                print("Estoy en modo oscuro")    
            funcion_a_decorar(args[0])
        return wrapper_interno
    

@DecoradorConArgumentos(Modo.CLARO)
def saludar(nombre):
    print("Hola",nombre)


saludar("Ricardo")