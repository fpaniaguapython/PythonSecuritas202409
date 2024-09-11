class DecoradorSimple:
    def __init__(self, funcion_a_decorar) -> None:
        self.funcion_a_decorar = funcion_a_decorar

    def escribir_log(self, *args, **kwargs):
        print("Escribiendo log...")

    def __call__(self, *args, **kwargs):
        self.escribir_log()
        print("Soy el decorador y estoy haciendo una tarea previa a la ejecución de la función")
        self.funcion_a_decorar(args[0])
        print("Soy el decorador y estoy haciendo una tarea posterior a la ejecución de la función")

'''
    def __call__(self, nombre):
        print("Soy el decorador y estoy haciendo una tarea previa a la ejecución de la función")
        self.funcion_a_decorar(nombre)
        print("Soy el decorador y estoy haciendo una tarea posterior a la ejecución de la función")
'''

@DecoradorSimple
def saludar(nombre):
    print("Hola",nombre)


saludar("Ricardo")