#Crear una función que sume un número indeterminado de números
#Decorar con un decorador (positivar) que convierta los números negativos en positivos

def positivador(funcion_a_decorar):
    def wrapper(*args):
        enteros = [abs(numero) for numero in args]
        return funcion_a_decorar(*enteros) #Ojo a la notación ya que tenemos que pasar los argumentos separados por coma       
    return wrapper

@positivador
def sumar(*args):
    return sum(args)

print(sumar(3,4,10))
print(sumar(3,-4,10))
