def sumar(a,b):
    return a+b
print(sumar(3,1))

sumar_lambda = lambda a,b: a+b
print(sumar_lambda(4,2))

print((lambda a,b:a+b)(1,8))#La segunda tupla son los argumentos que recibe la expresión


#Uso de filter 'normal'
def aceptar(numero):
    return numero>10

numeros = [8,10,12,80,50]
numeros_filtrados = filter(aceptar, numeros)
print(list(numeros_filtrados))

#Uso de filter con lambda
numeros = [8,10,12,80,50]
numeros_filtrados = filter(lambda numero : numero<=10, numeros)
print(list(numeros_filtrados))
