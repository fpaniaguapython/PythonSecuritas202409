#Función isinstance --> __instancecheck__(self, object)

#Función issubclass --> __subclasscheck__(self, subclass)

class Independiente:
    pass

class A:
    pass

class B(A):
    pass

objeto = B()

#Función isinstance
print(isinstance(objeto, Independiente))#False
print(isinstance(objeto, A))#True
print(isinstance(objeto, B))#True

#Función issubclass
print(issubclass(B,A))#True
print(issubclass(B,Independiente))#False

