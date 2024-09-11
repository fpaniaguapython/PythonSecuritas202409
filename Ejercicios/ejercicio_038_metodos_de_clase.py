class Artefacto:

    __longevidad = 0

    def __init__(self) -> None:
        Artefacto.__longevidad = 14 #Hacemos referencia a __longevidad a través de Artefacto

    @classmethod
    def mostrar(cls):
        print(cls.__longevidad) #Hacemos referencia a __longevidad a través de cls (es método de clase)
    
    @staticmethod
    def metodo_estatico():
        Artefacto.__longevidad =15 #Hacemos referencia a __longevidad a través de Artefacto

artefacto = Artefacto()
Artefacto.mostrar()#14
Artefacto.metodo_estatico()
Artefacto.mostrar()#15
#print(Artefacto.__longevidad)-->Error porque el atributo está 'oculto'
