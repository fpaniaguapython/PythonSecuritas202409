from Factura import Factura
from IGestorPersistencia import IGestorPersistencia
import pickle

class GestorPersistenciaPicke(IGestorPersistencia):
    def __get_nombre_fichero(self, numero:int):
        return str(numero)+".factura"
    def save(self, factura: Factura):
        with open(self.__get_nombre_fichero(factura.numero), 'wb') as fichero:
            pickle.dump(factura, fichero)

    def read(self, numero: int):
        with open(self.__get_nombre_fichero(numero), 'rb') as fichero:
            factura = pickle.load(fichero)
        return factura