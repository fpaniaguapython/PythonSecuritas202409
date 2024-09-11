class Artefacto:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre #Oculta al atributo

    #get 'clásico'
    def get_nombre(self):
        return self.__nombre

    #set 'clásico'
    def set_nombre(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

martillo = Artefacto("Martillo")
#print(martillo.__nombre)#KO -> AtributeError
#print(martillo.nombre)#KO -> AtributeError
print(martillo._Artefacto__nombre)#OK -> Martillo

print(martillo.get_nombre())#OK -> Martillo
martillo.set_nombre('Destornillador')#OK

print(martillo.nombre)#OK -> Destornillador
#martillo.nombre = "Taladradora" #KO -> AttributeError