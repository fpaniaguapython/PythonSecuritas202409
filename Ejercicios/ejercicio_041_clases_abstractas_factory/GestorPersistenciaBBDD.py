from GestorPersistencia import GestorPersistencia

class GestorBBDD(GestorPersistencia):
    def guardar(self, dato):
        self.registrar_accion("Se ha guardado un dato")
        print(f'Guardando {dato} en BBDD')

    def leer(self):
        self.registrar_accion("Se ha guardado un dato")
        print(f'Leyendo de BBDD')