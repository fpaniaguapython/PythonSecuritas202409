class Vehiculo: #Declaración de la clase
    def __init__(self, marca : str): #Constructor
        self.marca = marca #Atributo creado a partir del argumento del constructor
        self.modelo = "1430" #Atributo 

    def arrancar(self): #Método
        print("Arrancando...")

auto1 = Vehiculo("Seat")
auto1.arrancar()