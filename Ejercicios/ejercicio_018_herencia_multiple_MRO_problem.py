class Base:
    def saludar(self):
        print("Hola, soy Base")

class A(Base):
    #def saludar(self):
    #    print("Hola, soy A")
    def escribir(self):
        print("Escribiendo...")

class B(Base):
    def saludar(self):
        print("Hola, soy B")
    def leer(self):
        print("Leyendo...")

class C(Base,B):
    pass

objeto = C()
objeto.saludar() #TypeError: Cannot create a consistent method resolution order (MRO) for bases Base, B