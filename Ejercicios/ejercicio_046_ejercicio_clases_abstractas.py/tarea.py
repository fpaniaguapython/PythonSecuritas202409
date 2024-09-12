import abc
from parametro import Parametro

class Tarea(abc.ABC):
    def __init__(self, nombre : str, parametros : tuple[Parametro]) -> None:
        self.__nombre = nombre
        self.__parametros = parametros
        
    def mostrar_parametros(self):
        for parametro in self.__parametros:
            print(parametro)

    @property
    def parametros(self):
        return self.__parametros

    @abc.abstractmethod
    def ejecutar(self):
        pass