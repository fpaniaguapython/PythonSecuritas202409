class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre


p1 = Persona("Manuel")

print(Persona.__class__) #<class 'type'>
print(p1.__class__) #<class '__main__.Persona'
print(p1.nombre.__class__) #<class 'str'>