#Definición de una clase Cliente : Atributos nombre, dirección y número de teléfono
#Métodos para el envío de email
#Método que puestre los datos del cliente
#Crear una instancia, enviar el email y mostrar los datos

class Cliente:
    def __init__(self, nombre, direccion, numero_telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_telefono = numero_telefono

    def enviar_email(self, email):
        print("Enviando email...")
    
    def mostrar_datos(self):
        print(self.nombre)
        print(self.direccion)
        print(self.numero_telefono)


cliente1 = Cliente("Cleinte 1", "Direccion 1", "+3418374833")
cliente1.enviar_email("fernando@gmail.com")
cliente1.mostrar_datos()