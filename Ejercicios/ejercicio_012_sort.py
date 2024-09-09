class Cliente:
    def __init__(self, anyo_contratacion, facturacion_acumulada) -> None:
        self.anyo_contratacion = anyo_contratacion
        self.facturacion_acumulada = facturacion_acumulada

    def __repr__(self) -> str:
        return str(self.anyo_contratacion) + ":" + str(self.facturacion_acumulada)

    #Ordenar por facturación de menor a mayor
    #En caso de igual facturación, por año de más antiguo a más reciente
    def __lt__(self, other):
        is_less = False
        if (self.facturacion_acumulada == other.facturacion_acumulada):
            is_less = self.anyo_contratacion < other.anyo_contratacion
        else:
            is_less = self.facturacion_acumulada < other.facturacion_acumulada
        return is_less

c1 = Cliente(2012, 300_000)
c2 = Cliente(2021, 500_000)
c3 = Cliente(1999, 500_000)
c4 = Cliente(2022, 30_000)

clientes = [c1, c2, c3, c4]
clientes.sort()
print(clientes)


