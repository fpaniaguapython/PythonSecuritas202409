class FacturaException(Exception):
    pass


class FacturaSinImporteException(FacturaException):
    pass


class FacturaConImporteNegativoException(FacturaException):
    pass


class Factura:
    def __init__(self, numero_factura):
        if (type(numero_factura)!=int):
            raise FacturaException()


try:
    f = Factura("1384783")
except FacturaException:
    print("Ha ocurrido una FacturaException")

