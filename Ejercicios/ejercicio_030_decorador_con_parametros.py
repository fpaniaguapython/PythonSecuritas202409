def decorador(entorno): #Decorador recibe parámetros de decoración
    print("Estoy en el decorador:",entorno)
    def wrapper(funcion_a_decorar): #El 'wrapper' recibe la función a decorar
        print("Estoy en el wrapper externo:",entorno)
        def wrapper_interno(nombre): #El 'wrapper interno' recibe los parámetros de la función a decorar 
            print("Estoy en el wrapper interno:",entorno)
            funcion_a_decorar(nombre)
        return wrapper_interno
    return wrapper

@decorador('oscuro')
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Domingo')