def f1(nombre, *args, **kwargs):
    f3(nombre, *args, **kwargs) #OJO A LA NOTACIÓN DE LOS PARÁMETROS (En la función de destino se 'respeta' la estructura)

def f2(nombre, *args, **kwargs): 
    f4(nombre, args, kwargs) #OJO A LA NOTACIÓN DE LOS PARÁMETROS

def f3(nombre, *args, **kwargs):
    print(nombre) #Python
    print('*args:', args) #Tupla -> *args: (1, 2, 3)
    print('**kwargs:', kwargs) #Diccionario -> **kwargs: {'x': 4, 'y': 5, 'z': 6}

def f4(nombre, *args, **kwargs):
    print(nombre) #Python
    print('*args:', args) #Tupla -> *args: ((1, 2, 3), {'x': 4, 'y': 5, 'z': 6})
    print('**kwargs:', kwargs) #Dicccionario -> **kwargs: {}


f1("Python", 1, 2, 3, x=4, y=5, z=6)
f2("Python", 1, 2, 3, x=4, y=5, z=6)

