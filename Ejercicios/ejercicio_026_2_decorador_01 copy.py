def decorador_simple(funcion):
    print("Acción periférica")
    return funcion

@decorador_simple
def saludar():
    print("Hola")

saludar()