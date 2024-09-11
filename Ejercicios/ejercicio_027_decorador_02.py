def decorador_simple(funcion_a_decorar):
    def wrapper(nombre):
        print(f"Soy un decorador y estoy saludando a {nombre}") #Acción periférica
        funcion_a_decorar(nombre) #Acción principal (podría no ejecutarse ignorando el comportamiento original de la función)
        print("Soy el decorador y he terminado mi trabajo") #Acción periférica
    return wrapper


@decorador_simple
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Fernando")

#Crear una función que sume dos números
#Decorar con un decorador (positivar) que convierta los números negativos en positivos
