import sqlite3
from Factura import Factura
from IGestorPersistencia import IGestorPersistencia

class GestorPersistenciaSQLite(IGestorPersistencia):
    NOMBRE_BBDD = 'dbfacturas.sqlite'
    MODELO_DE_DATOS = 'CREATE TABLE IF NOT EXISTS tfacturas(numero INTEGER PRIMARY KEY, cliente TEXT NOT NULL, importe INTEGER NOT NULL)'

    def __init__(self):
        self.conexion = sqlite3.connect(GestorPersistenciaSQLite.NOMBRE_BBDD)
        cursor = self.conexion.cursor()
        cursor.execute(GestorPersistenciaSQLite.MODELO_DE_DATOS)
        self.conexion.commit()
        cursor.close()

    def __del__(self):
        self.conexion.close()

    def save(self, factura: Factura):
        cursor = self.conexion.cursor()
        cursor.execute(f"INSERT INTO tfacturas (numero, cliente, importe) VALUES ({factura.numero}, '{factura.cliente}',{factura.importe})")
        self.conexion.commit()
        cursor.close()

    def read(self, numero: int):
        cursor = self.conexion.cursor()
        datos_factura = cursor.execute(f"SELECT * FROM tfacturas WHERE numero={numero}").fetchone()
        factura = Factura(*datos_factura)
        cursor.close()
        return factura