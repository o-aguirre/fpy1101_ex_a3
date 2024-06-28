#Crear una función que revisa una lista de números la cual será ingresada mediante input por el usuario,
#debe obtener el promedio de esta lista según la cantidad de números que existan en la lista

def obtener_lista():
    lista = []
    while True:
        opt = input('Desea agregar un numero a la lista? s/n: ')
        if opt == 's':
            elemento = int(input('Ingrese un número: '))
            lista.append(elemento)
        else:
            return lista
    
def promedio():
    lista = obtener_lista()
    cont = 0
    total = 0
    for i in lista:
        cont += 1
        total += i
    return total / cont

print(promedio())