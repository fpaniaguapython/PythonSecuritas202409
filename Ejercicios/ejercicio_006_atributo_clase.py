class Persona:
    esperanza_vida = 89 #Declaración de un variable de clase

    def __init__(self, nombre):
        self.nombre = nombre

patricia = Persona("Patricia")
fernando = Persona("Fernando")

print(fernando.nombre)#'Fernando'

print(Persona.esperanza_vida)#89
print(fernando.esperanza_vida)#89
print(patricia.esperanza_vida)#89

Persona.esperanza_vida = 90
print(Persona.esperanza_vida)#90
print(fernando.esperanza_vida)#90
print(patricia.esperanza_vida)#90

fernando.esperanza_vida = 91 #Construye un atributo de instancia
print(Persona.esperanza_vida)#90
print(fernando.esperanza_vida)#91
print(patricia.esperanza_vida)#90
    
