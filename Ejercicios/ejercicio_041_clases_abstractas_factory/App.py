from GestorPersistencia import GestorPersistencia
from GestorFactory import PersistenceFactory

if __name__ == '__main__':
    persistencia = PersistenceFactory.get_gestor()
    if (isinstance(persistencia, GestorPersistencia)):
        persistencia.guardar("El dato")
        persistencia.leer()
    else:
        print("Error")