#Comprensión de listas

#list comprehension

lista_dias = ['Lunes','Martes','Miércoles','Jueves','Viernes', 'Sábado', 'Domingo']

#Método 'tradicional'
lista_mayusculas = []
for dia in lista_dias:
    lista_mayusculas.append(dia.upper())
print(lista_mayusculas)

#Método Python
lista_minusculas = [dia.lower() for dia in lista_dias ]
print(lista_minusculas)

#Con llamada a función
def obtener_longitud(texto):
    return len(texto)

lista_longitudes = [obtener_longitud(dia) for dia in lista_dias]
print(lista_longitudes)

#Con llamada a método
class Cliente:
    def __init__(self, nombre, saldo) -> None:
        self.nombre = nombre
        self.saldo = saldo
    
    def obtener_mensaje(self):
        return self.nombre + " tu saldo es " + str(self.saldo)
    
c1 = Cliente("Fernando", 500)
c2 = Cliente("Ismael", 3000)
c3 = Cliente("Arturo", 800)
c4 = Cliente("Sara", -300)
lista_clientes = [c1, c2, c3, c4]

lista_mensajes = [cliente.obtener_mensaje() for cliente in lista_clientes]
print(lista_mensajes)

#Con llamada a método y con condición

lista_mensajes_morosos = [cliente.obtener_mensaje() for cliente in lista_clientes if cliente.saldo<0]
print(lista_mensajes_morosos)