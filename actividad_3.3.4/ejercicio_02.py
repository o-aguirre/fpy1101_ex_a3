#Crear función que me retorne un valor booleano en caso que el número sea Par

num = int(input('Ingrese un numero: '))

def par(numero):
    if numero % 2 == 0:
        return True

print(par(num))