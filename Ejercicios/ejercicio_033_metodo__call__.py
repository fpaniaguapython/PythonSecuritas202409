class Artefacto:
    def __init__(self, elemento) -> None:
        self.elemento = elemento
    def __call__(self, *args, **kwargs):
        print("Ejecutando la acción:", args[0])
    
catapulta = Artefacto("piedra")
catapulta("lanzar")
