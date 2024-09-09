#Los atributos de instancia se pueden crear:
# En el constructor
# En los métodos de instancia
# Fuera de la clase, sobre el propio objeto
class Lenguaje:
    def __init__(self, nombre):
        self.nombre = nombre #Variable de instancia
        self.activo = True #Variable de instancia
    
    def mostrar(self):
        self.mostrado = True #Variable de instancia creada en un método


l1 = Lenguaje("Python")
l2 = Lenguaje("Java")
l3 = Lenguaje("C++")

l2.mostrar() #La llamada tiene como consecuencia la creación del atributo mostrado
l2.favorito = False #Variable de instancia creada fuera de la clase

print(l2.__dict__) #{'nombre': 'Java', 'activo': True, 'mostrado': True, 'favorito': False}