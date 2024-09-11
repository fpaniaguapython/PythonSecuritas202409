def decorador_simple(funcion):
    print("Acción periférica")
    return funcion

def saludar():
    print("Hola")

saludar_decorada = decorador_simple(saludar)

saludar_decorada()