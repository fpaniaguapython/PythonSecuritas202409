def recibir_llamada(cliente):
    print(f"Recibiendo llamada de {cliente}")

def crear_ficha(cliente):
    print(f"Creando ficha de {cliente}")

def establecer_contacto(cliente):
    print(f"Estableciendo contacto de {cliente}")

def facturar(cliente):
    print(f"Facturando a de {cliente}")

proceso_facturacion = facturar #Asignación de una función a una variable

flujo_trabajo = [recibir_llamada, crear_ficha, establecer_contacto, proceso_facturacion]

for trabajo in flujo_trabajo:
    trabajo('Fernando') #Invocación a la función almacenada en el flujo de trabajo