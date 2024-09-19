def generar_funcion(nombre):
    mensaje = f'Hola {nombre}'
    def generar_funcion_demorada():
        print(mensaje)
    return generar_funcion_demorada

nombre = "Fernando"
funcion = generar_funcion(nombre)
nombre = "Miguel"
print(nombre)
funcion()
