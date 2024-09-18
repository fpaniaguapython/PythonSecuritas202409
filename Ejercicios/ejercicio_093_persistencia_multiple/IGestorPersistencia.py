import abc
from abc import abstractmethod

from Factura import Factura


class IGestorPersistencia(abc.ABC):
    @abstractmethod
    def save(self, factura : Factura):
        pass

    @abstractmethod
    def read(self, numero : int):
        pass