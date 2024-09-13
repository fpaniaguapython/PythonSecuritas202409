def sumar(s1, s2):
    if (s1<0 or s2<0):#Es un error, no se admiten sumandos negativos
        raise Exception() #A partir de este punto la función se interumpe
    resultado = s1 + s2
    return resultado

try :
    resultado = sumar(5,-8)
    print(resultado)#No se ejecuta si la línea anterior ha generado un error
except:
    print("Ha ocurrido un error")
