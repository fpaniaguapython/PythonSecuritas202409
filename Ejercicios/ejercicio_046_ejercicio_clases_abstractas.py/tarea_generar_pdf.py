from parametro import Parametro
from tarea import Tarea

class GeneradorPDFTarea(Tarea):
    def __init__(self, nombre: str, parametros: tuple[Parametro]) -> None:
        super().__init__(nombre, parametros)

    def ejecutar(self):
        print(f'Generando fichero {self.parametros[0].valor}.pdf con el texto {self.parametros[1].valor}')
        return