class MiException(Exception):
    pass


def chequear():
    try:
        elemento_inexistente = lista[4]
    except IndexError as ie:
        raise MiException("Mi información") from ie #La excepción nueva parte de una existente (ie)


lista = [3,4,8]

try:
    chequear()
except MiException as mi:
    print("La información de la excepción interna:", mi)
    print("La información de la excepción externa:", mi.__cause__)