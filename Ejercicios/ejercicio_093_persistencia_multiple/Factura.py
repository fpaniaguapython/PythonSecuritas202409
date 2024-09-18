class Factura:
    def __init__(self, numero, cliente, importe):
        self.numero = numero
        self.cliente = cliente
        self.importe = importe

    def __str__(self):
        return (f'{self.numero}:{self.cliente}:{self.importe}')