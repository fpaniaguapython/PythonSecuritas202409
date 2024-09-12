class Parametro:
    def __init__(self, nombre, valor) -> None:
        self.nombre = nombre
        self.valor = valor

    def __str__(self):
        return f'Nombre:{self.nombre} - Valor:{self.valor}'