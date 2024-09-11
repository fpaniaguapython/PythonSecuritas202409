from enum import Enum

class TipoPersistencia(Enum):
    FILE = 0
    BBDD = 1
    MELON = 2

TIPO_PERSISTENCIA = TipoPersistencia.FILE