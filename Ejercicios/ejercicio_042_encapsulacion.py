class Artefacto:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre #Oculta al atributo

    #Método oculto
    def __metodo_privado(self):
        pass
    
    ###
    ###ENCAPSULACIÓN CON EL MÉTODO 'CLÁSICO'
    ###Se accede a través de los métodos de acceso ('getter' y 'setter')
    ###

    #get 'clásico'
    def get_nombre(self):
        return self.__nombre

    #set 'clásico'
    def set_nombre(self, nombre):
        self.__nombre = nombre

    ###
    ###ENCAPSULACIÓN CON ANOTACIONES
    ###Se accede a través del nombre del atributo
    ###

    #get mediante @property
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @nombre.deleter
    def nombre(self):
        print("Método que se ejecuta cuando se ejecuta delattr")
        self.__nombre = None


###
###ENCAPSULACIÓN CON EL MÉTODO 'CLÁSICO'
###Se accede a través de los métodos de acceso ('getter' y 'setter')
###

martillo = Artefacto("Martillo")
#print(martillo.__nombre)#KO -> AtributeError
#print(martillo.nombre)#KO -> AtributeError
print(martillo._Artefacto__nombre)#OK -> Martillo

print(martillo.get_nombre())#OK -> Martillo
martillo.set_nombre('Destornillador')#OK

print("ACCESO A TRAVÉS DEL @PROPERTY:", martillo.nombre)#OK -> Destornillador
#martillo.nombre = "Taladradora" #KO -> AttributeError

martillo.nombre = "Sacacorchos"#OK
print(martillo.nombre)#Sacacorchos

delattr(martillo, "nombre")
print(martillo.nombre)