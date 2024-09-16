nombre = "Python"
nombres = ["Pithon", "C++", "Java"]
numero = 3
numeros = [8, 4, 2]

def cambiar_nombre(nombre : str):
    nombre = nombre + "*"

def cambiar_nombres(nombres : list):
    nombres[0]="Python" 


def cambiar_numero(numero : int):
    numero = 10

def cambiar_numeros(numeros : list):
    numeros[0] = 10

cambiar_nombre(nombre) #Paso de parámetro por valor
cambiar_nombres(nombres) #Paso de parámetros por referencia
cambiar_numero(numero) #Paso de parámetros por valor
cambiar_numeros(numeros) #Paso de parámetros por referencia

print(nombre) #Python
print(nombres) #['Python', 'C++', 'Java']
print(numero) #3
print(numeros) #[10, 4, 2]




