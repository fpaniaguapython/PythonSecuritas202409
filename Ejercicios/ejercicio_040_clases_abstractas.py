import abc

class GestorPersistencia(abc.ABC):
    def __init__(self) -> None:
        pass

    def escribir_log(self, texto):
        print("Log:", texto)

    @abc.abstractmethod
    def write(self, objeto):
        pass

#gp = GestorPersistencia() #Error que garantiza que no se pueden crear instancias de clases abstractas

class GestorPersistenciaFichero(GestorPersistencia):
    def write(self, objeto):
        pass

gp = GestorPersistenciaFichero() #Ok