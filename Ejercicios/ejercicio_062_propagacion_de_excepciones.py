#Propagación de excepciones

def f1(numero):
    if (numero==0):
        raise ValueError("Error: el número es 0")
    

def f2(numero):
    try:
        f1(numero)
    except ValueError as ve:
        print("Hacemos algo con el error")
        raise ve
    

try:
    f2(0)
except ValueError as ve:#ve es la excepción que se creó y lanzó en la línea 5
    print(ve)