import enum

class TipoFacturaException(enum.Enum):
    NUMERO_FACTURA_NO_INT = 0
    IMPORTE_FACTURA_NO_INT = 1
    IMPORTE_FACTURA_NO_POSITIVO = 2
    IMPORTE_IMPAR = 3

class FacturaException(Exception):
    def __init__(self, tipo : TipoFacturaException, *args: object) -> None:
        super().__init__(*args)
        self.tipo = tipo

class Factura:
    def __init__(self, numero_factura, importe):
        if (type(numero_factura)!=int):
            raise FacturaException(TipoFacturaException.NUMERO_FACTURA_NO_INT, "El número de la factura no es un int")
        if (type(importe)!=int):
            raise FacturaException(TipoFacturaException.IMPORTE_FACTURA_NO_INT, "El importe de la factura no es un int")
        if (importe<=0):
            raise FacturaException(TipoFacturaException.IMPORTE_FACTURA_NO_POSITIVO, "El importe de la factura debe ser positivo")
        if (importe%2!=0):
            raise FacturaException(TipoFacturaException.IMPORTE_IMPAR, "No nos gustan los números impares")

try:
    #f1 = Factura("DOS", 100)
    f2 = Factura(1000, 87)
    #f3 = Factura(1384783, 100)#Correcto
    print("La factura se ha creado correctamente")
except FacturaException as fe:
    match fe.tipo:
        case TipoFacturaException.NUMERO_FACTURA_NO_INT:
            print("Acción 1")
        case TipoFacturaException.IMPORTE_FACTURA_NO_INT:
            print("Acción 2")
        case TipoFacturaException.IMPORTE_FACTURA_NO_POSITIVO:
            print("Acción 3")
        case _:#Opción por defecto
            print("Acción por defecto")
    