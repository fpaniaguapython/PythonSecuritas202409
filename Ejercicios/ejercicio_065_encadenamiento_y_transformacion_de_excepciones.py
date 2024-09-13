class MiException(Exception):
    pass

def chequear(lista):
    try:
        elemento_inexistente = lista[4]
    except IndexError as ie:
        raise MiException("Mi información - IndexError") from ie

def comprobar(lista):
    try:
        dato = lista[0]/0
    except ZeroDivisionError as zde:
        raise MiException("Mi información - ZeroDivisionError") from zde

lista_elementos_a_verificar = (3,4,8)
lista_funciones_de_verificacion = (chequear, comprobar)

for verificacion in lista_funciones_de_verificacion:
    try:
        verificacion(lista_elementos_a_verificar)
    except MiException as me:
        print("La información de la excepción externa:", me.__cause__)