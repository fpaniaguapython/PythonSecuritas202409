import json

from GestorPersistenciaJSON import GestorPersistenciaJSON
from GestorPersistenciaPickle import GestorPersistenciaPicke
from GestorPersistenciaSQLite import GestorPersistenciaSQLite


class GestorPersistenciaFactory:
    gestor_persistencia = None
    @classmethod
    def get_gestor_persistencia(cls):
        if (cls.gestor_persistencia==None):
            with open('config.json') as f_config:
                configuracion = json.load(f_config)
                tipo_persistencia = configuracion['tipo-persistencia']
                if (tipo_persistencia=='SERIALIZACION'):
                    cls.gestor_persistencia = GestorPersistenciaPicke()
                elif (tipo_persistencia=='JSON'):
                    cls.gestor_persistencia = GestorPersistenciaJSON()
                elif (tipo_persistencia=='SQLITE'):
                        cls.gestor_persistencia = GestorPersistenciaSQLite()
                elif (tipo_persistencia=='ENGENDRO'):
                        cls.gestor_persistencia = "ENGENDRO"
        return cls.gestor_persistencia
