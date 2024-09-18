from Factura import Factura
from GestorPersistenciaFactory import GestorPersistenciaFactory
from IGestorPersistencia import IGestorPersistencia

if __name__=='__main__':
    gp = GestorPersistenciaFactory.get_gestor_persistencia()
    if (isinstance(gp, IGestorPersistencia)):
        f5 = Factura(5, "Cliente 5",5000)
        gp.save(f5)

        f5 = gp.read(5)
        print(type(f5))
        print(f5)
    else:
        print("Ha ocurrido un error, el GestorPersistencia proporcionado no es correcto")
