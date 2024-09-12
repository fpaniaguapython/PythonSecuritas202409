from enum import Enum

class Tipo(Enum):
    GASOLINA = 0
    DIESEL = 1
    HIBRIDO = 2
    ELECTRICO = 3

class Motor:
    __numero_motores_electricos = 0
    def __init__(self, tipo) -> None:
        self.tipo = tipo
        if (self.tipo==Tipo.ELECTRICO):
            Motor.__numero_motores_electricos+=1

    @staticmethod
    def get_numero_motores_electricos():
        return Motor.__numero_motores_electricos
        

Motor(Tipo.DIESEL)
Motor(Tipo.ELECTRICO)
Motor(Tipo.ELECTRICO)
Motor(Tipo.DIESEL)
Motor(Tipo.ELECTRICO)
print(Motor.get_numero_motores_electricos())



