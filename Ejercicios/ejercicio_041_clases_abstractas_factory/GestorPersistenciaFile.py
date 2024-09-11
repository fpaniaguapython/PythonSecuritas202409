from GestorPersistencia import GestorPersistencia

class GestorFile(GestorPersistencia):
    def guardar(self, dato):
        self.registrar_accion("Se ha guardado un dato")
        print(f'Guardando {dato} en fichero')

    def leer(self):
        self.registrar_accion("Se ha escrito un dato")
        print(f'Leyendo de fichero')