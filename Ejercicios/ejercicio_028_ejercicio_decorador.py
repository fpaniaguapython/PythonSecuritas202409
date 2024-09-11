#Crear una función que sume dos números
#Decorar con un decorador (positivar) que convierta los números negativos en positivos

def positivador1(funcion_a_decorar):
    def wrapper(s1, s2):
        s1 = abs(s1)
        s2 = abs(s2)
        return funcion_a_decorar(s1, s2)        
    return wrapper

def positivador2(funcion_a_decorar):
    def wrapper(*args):
        s1 = abs(args[0])
        s2 = abs(args[1])
        return funcion_a_decorar(s1, s2)        
    return wrapper

@positivador1
def sumar1(s1, s2):
    return s1 + s2

@positivador2
def sumar2(s1, s2):
    return s1 + s2

print(sumar1(3,4))
print(sumar2(3,-4))

print(sumar1(8,-4))
print(sumar2(8,4))
