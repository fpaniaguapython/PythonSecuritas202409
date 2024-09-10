def funcion1():
    pass

funcion1()

def funcion2(argumento1, argumento2):
    print(f'Argumento 1:{argumento1}')
    print(f'Argumento 2:{argumento2}')

funcion2(3, 8) #Posicionales
funcion2(argumento2=10, argumento1=5)

def funcion3(argumento1, argumento2=10):
    print(f'Argumento 1:{argumento1}')
    print(f'Argumento 2:{argumento2}')

funcion3(1)
funcion3(2,3)

# def funcion4(argumento1=10, argumento2): #ERROR, el argumento con valor por defecto debe ir al final

def funcion5(argumento1, argumento2=5, argumento3=8):
    pass

# *args recibe un número indeterminado de valores como una tupla
def funcion5(*args):
    print(type(args))
    for arg in args:
        print(arg)

# La llamada a *args es una sucesión de argumentos separados por coma
funcion5("T1")
funcion5("T1","T2")
funcion5("T1","T2","T3")

def funcion6(argumento1, argumento2, *args):
    print(argumento1)
    print(argumento2)
    for arg in args:
        print("*" + str(arg))

funcion6(1,3)
funcion6(1,3,8)
funcion6(1,3,8,4)

def funcion7(*args, argumento1):
    print(argumento1)
    for arg in args:
        print("*" + str(arg))

#funcion7(3)#Error
#funcion7(3,8)#Error
#funcion7(3,8,4)#Error

funcion7(argumento1=3)
#funcion7((4,5,8),3)#Error
funcion7((4,5,8),argumento1=3)
funcion7(4,5,7,argumento1=3)

def funcion8(**kwargs):
    print(type(kwargs))#<class 'dict'>
    
    for k in kwargs.keys():
        print(k)
    
    for v in kwargs.values():
        print(v)
    
    for k,v in kwargs.items():
        print(k + ":" + str(v))

funcion8(argumento1=10, argumento2=20)

def funcion9(**kwargs):
    pass

funcion9(argumento1=10, argumento2=20)

def funcion9_1(argumento1, **kwargs):
    pass

funcion9_1(1, x=10, y=10)

def funcion9_2(argumento2=10, **kwargs):
    pass

funcion9_2(argumento2=8, x=10, y=10)

def funcion10(*args, **kwargs):
    pass

funcion10(3, 4, edad=30, saldo=5_000)

def funcion11(*args, saldo=5000, **kwargs):
    pass

funcion11(3,4,saldo=3000,edad=80)

#Ejemplo MÁS COMPLETO 
def funcion_multiple(a, b, *args, c=20, d=40, **kwargs):
    print(f'p:{a}')
    print(f'p:{b}')
    for arg in args:
        print(f'*:{arg}')
    print(f'n:{c}')
    print(f'n:{d}')
    for k,v in kwargs.items():
        print(f'**:{k}:{v}')

funcion_multiple(1,2,3,4,c=5,d=6,e=7,f=8,g=9)