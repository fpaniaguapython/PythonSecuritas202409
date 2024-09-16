#Creamos una lista de 3 tuplas que contienen (número_factura, nombre_cliente, importe)
#Crear una función que almacene en ficheros las facturas 
#Hay un fichero para facturas de >10_000€ de importe
#Otro distinto para el resto

#El script tiene la evaluación __name__=='__main__'
#Cuando se arranque la aplicación, se intente leer el fichero, cargar los objetos y
#mostrarlos por pantalla
import pickle
import os

IMPORTE_MINIMO = 10_000
F_FACTURAS_MAXI = 'facturas_maxi.fac'
F_FACTURAS_MINI = 'facturas_mini.fac'

facturas = [("Numero1","Cliente1",5_000),("Numero2","Cliente2",25_000),("Numero3","Cliente3",8_000)]

def guardar_factura(nombre_fichero, factura):   
    with open(nombre_fichero,'ab') as fichero:
                pickle.dump(factura, fichero)

def almacenar_facturas(facturas : list) -> None:
    for factura in facturas:
        if (factura[2]>IMPORTE_MINIMO):
            guardar_factura(F_FACTURAS_MAXI, factura)
        else:
            guardar_factura(F_FACTURAS_MINI, factura)

if __name__=='__main__':
    facturas_maxi = []
    facturas_mini = []
    if (not os.path.exists(F_FACTURAS_MAXI)):
         almacenar_facturas(facturas)
    else:
        try:
            with open(F_FACTURAS_MAXI, 'rb') as fichero:
                while True:
                    facturas_maxi.append(pickle.load(fichero))
        except EOFError as ee:
            print("Fichero leido y procesado")
        finally:
            print(facturas_maxi)

        try:
            with open(F_FACTURAS_MINI, 'rb') as fichero:
                while True:
                    facturas_mini.append(pickle.load(fichero))
        except EOFError as ee:
            print("Fichero leido y procesado")
        finally:
            print(facturas_mini)