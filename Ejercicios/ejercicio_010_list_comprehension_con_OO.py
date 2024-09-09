#Crear una clase Cliente (nombre, email, saldo)
#Crear la clase Mensaje
#Crear una lista con 3 clientes, dos de los cuales tienen saldo negativo (-300, -500)
#Utilizando comprensión de listas, crear una lista de objetos con la dirección de correo 
# y el textos que se les enviaría a los clientes con saldo negativo >400 

class Cliente:
    def __init__(self, nombre, email, saldo):
        self.nombre = nombre
        self.email = email
        self.saldo = saldo

class Mensaje:
    def __init__(self, email, texto) -> None:
        self.email = email
        self.texto = texto

    def __str__(self) -> str:
        return self.email + ":" + self.texto
    
    def __repr__(self) -> str:
        pass

c1 = Cliente("C1","c1@gmail.com",100)
c2 = Cliente("C2","c2@gmail.com",-300)
c3 = Cliente("C3","c3@gmail.com",-500)

clientes = [c1, c2, c3]

mensajes_para_clientes_muy_morosos = [Mensaje(cliente.email, "Debes mucho dinero") 
                                      for cliente in clientes 
                                      if cliente.saldo<-400]

for mensaje in mensajes_para_clientes_muy_morosos: 
    print(mensaje)