from parametro import Parametro
from tarea import Tarea

class CorreoTarea(Tarea):
    def __init__(self, nombre: str, parametros: tuple[Parametro]) -> None:
        super().__init__(nombre, parametros)

    def ejecutar(self):
        print(f'Enviando correo electronico a {self.parametros[0].valor}: {self.parametros[1].valor}')
        return