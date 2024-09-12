# Clase Factura. Atributos nombre, importe (está en euros). 
# Atributos son privados y tienen métodos de acceso a través de decoradores.
#
# Crear una función mostrarImporte a la que se pasa un objeto factura y muestra los datos por pantalla
#
# Decorador para la función mostrarImporte va a recibir un argumento que va ser EURO o DOLAR de una enumeración 
# El decorador va poner el símbolo correspondiente y a modificar el importe si es DOLAR (cambio de divisa)

#Creo una factura de 1000 euros de importe.
#Al llamar función mostrarImporte indico si quiero mostrarlo en dólares o en euros.
#Si es en euros, mostramos 1000€.
#Si es en dólares, mostramos 950$
import enum

class TipoMoneda(enum.Enum):
    EURO = 1
    DOLAR = 2

class Factura:
    def __init__(self, nombre, importe) -> None:
        self.__nombre = nombre
        self.__importe = importe


    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def importe(self):
        return self.__importe
    
    @importe.setter
    def importe(self, importe):
        self.__importe = importe
    

def mostrar_importe(tipo_moneda : TipoMoneda):
    def wrapper_externo(funcion_a_decorar):
        def wrapper_interno(factura):
            importe = factura.importe
            simbolo = ""
            resultado = 0
            if (tipo_moneda==TipoMoneda.DOLAR):
                simbolo = '$'
                resultado = importe*0.95
            elif (tipo_moneda==TipoMoneda.EURO):
                simbolo = "€"
                resultado = importe

            #Solución 1. Modificando el importe de la factura
            #factura.importe = resultado #Inquietante: el decorador modifica la factura
            #funcion_a_decorar(factura)
            #print(simbolo)

            #Solución 2. Sustituyendo el comportamiento de la función decorada
            #print(f'{resultado}{simbolo}')

            #Solución 3. Creando una factura nueva con el importe convertido
            funcion_a_decorar(Factura(factura.nombre, resultado))
            print(simbolo)

        return wrapper_interno
    return wrapper_externo

@mostrar_importe(TipoMoneda.DOLAR)
def mostrar_importe(factura : Factura):
    print(factura.importe, end="")

factura = Factura("Nombre",1000)

mostrar_importe(factura)

print(factura.importe)