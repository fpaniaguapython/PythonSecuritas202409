#Encadenamiento de excepciones
#__context__ --> Propio de las excepciones que se encadenan de forma implícito
#__cause__ --> Propia de las excepciones que se encadenan de forma explícito

lista = ['Elemento 1', 'Elemento 2']


try:
    lista[2]
except IndexError as ie:
    try:
        dato = 1/0
    except ZeroDivisionError as zde:
        print("Excepción interna:", zde)
        print("Excepción externa:", ie)
        print("Referencia a la excepción externa:", zde.__context__)
        print(zde.__context__ is ie) #True --> Indica que zde.__context__ es ie
