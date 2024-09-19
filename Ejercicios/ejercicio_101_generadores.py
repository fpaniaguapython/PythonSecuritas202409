import time

NUMERO_ELEMENTOS = 100

class Factura:
    def __init__(self, numero) -> None:
        self.numero = numero

def funcion_generacion():
    for factura in range(NUMERO_ELEMENTOS):
        time.sleep(2)
        yield Factura(factura)

for factura in funcion_generacion():
    print(factura.numero)
