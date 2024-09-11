from GestorPersistenciaBBDD import GestorBBDD
from GestorPersistenciaFile import GestorFile
from config import TipoPersistencia #Enumeración
from config import TIPO_PERSISTENCIA #Tipo

class PersistenceFactory:
    gestor = None

    @classmethod
    def get_gestor(cls):
        if (cls.gestor==None):
            if (TIPO_PERSISTENCIA==TipoPersistencia.FILE):
                cls.gestor = GestorFile()
            elif (TIPO_PERSISTENCIA==TipoPersistencia.BBDD):
                cls.gestor = GestorBBDD()
            elif (TIPO_PERSISTENCIA==TipoPersistencia.MELON):
                cls.gestor = "Melón"
        return cls.gestor