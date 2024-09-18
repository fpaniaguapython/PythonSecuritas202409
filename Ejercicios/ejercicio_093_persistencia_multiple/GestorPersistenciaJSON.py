from Factura import Factura
from IGestorPersistencia import IGestorPersistencia
import json

class GestorPersistenciaJSON(IGestorPersistencia):
    def __get_nombre_fichero(self, numero:int):
        return str(numero)+".json"

    def save(self, factura: Factura):
        with open(self.__get_nombre_fichero(factura.numero), 'w') as fichero:
            json.dump(factura.__dict__, fichero)

    def read(self, numero: int):
        with open(self.__get_nombre_fichero(numero), 'r') as fichero:
            datos_factura = json.load(fichero)
            #factura = Factura(datos_factura['numero'],datos_factura['cliente'],datos_factura['importe'])
            factura = Factura(*datos_factura.values()) #Si el constructor recibe todos los atributos almacenados en el JSON
        return factura