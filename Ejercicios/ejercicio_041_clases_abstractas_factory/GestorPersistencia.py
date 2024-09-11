import abc

class GestorPersistencia(abc.ABC):
    def registrar_accion(self, texto):
        print("Ha ocurrido algo:",texto)

    @abc.abstractmethod
    def guardar(self, dato):
        pass

    @abc.abstractmethod
    def leer(self):
        pass