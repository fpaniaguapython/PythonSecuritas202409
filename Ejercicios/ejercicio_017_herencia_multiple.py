class A:
    def saludar(self):
        print("Hola, soy A")
    def escribir(self):
        print("Escribiendo...")

class B:
    def saludar(self):
        print("Hola, soy B")
    def leer(self):
        print("Leyendo...")

class C(B,A):
    pass

objeto = C()
print(type(objeto)) #<class '__main__.C'>
print(isinstance(objeto, A))#True
print(isinstance(objeto, B))#True
print(isinstance(objeto, C))#True

objeto.leer()
objeto.escribir()

objeto.saludar()#Hola, soy A si el orden es (A,B); Hola, soy B si el orden es (B,A))
