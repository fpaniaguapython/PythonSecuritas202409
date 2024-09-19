
def saludar(nombre : str) -> str:
    '''
    Devuelve la cadena 'Hola nombre' donde 'nombre' es el valor del argumento recibido
    '''
    return f'Hola {nombre}'


#Además de mostrar el texto descriptivo de la función en la ayuda contextual, se muestra cuando se utiliza la función help
print(help(saludar))