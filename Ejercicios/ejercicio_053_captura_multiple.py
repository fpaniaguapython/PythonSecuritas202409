#Sumador de números enteros positivos
def sumar(s1 : int, s2 : int) -> int:
    if (type(s1)!=int or type(s2)!=int):
        raise TypeError("Los tipos de los sumandos deben ser positivos") #TypeError porque estamos verificando el tipo
    if (s1<0 or s2<0):
        raise ValueError("Los valores de los sumandos deben ser positivos") #ValueError porque estamos verificando el valor
    return s1+s2

try:
    #resultado = sumar(2,3)#OK --> 5
    #sumar("tres",2) #Provoca TypeError
    resultado = sumar(-3,3)
    print(resultado)
except (TypeError, ValueError) as te:#Captura de múltiples tipos
    print("Entrando por el except de TypeError o ValueError")
    print(te)
except Exception as e:
    print("Ha ocurrido un error no controlado:")
    print(e)