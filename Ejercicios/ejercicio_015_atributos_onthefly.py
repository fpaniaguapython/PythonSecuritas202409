class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

perro = Animal("Manchitas")

#Asignamos un nuevo atributo al perro (patas)
perro.numero_patas = 4

gato = Animal("Miseria")

#El perro tiene patas, NO PROBLEM
print(perro.numero_patas)

#Estamos verificando si el gato tiene patas
if (hasattr(gato, "numero_patas")):
    print(gato.numero_patas)
else:
    print("El gato no tiene patas")