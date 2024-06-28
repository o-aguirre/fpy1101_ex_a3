#Crear una aplicación en donde pueda tener las siguientes opciones:
#- Sumar números.
#- Multiplicar números.
#- Cantidad de números pares e impares.
#- Obtener promedio de los números ingresados.
#- Obtener la suma de los factoriales de cada número

def obtener_numeros():
    num_list = []
    while True:
        num = int(input('Ingresa numero: '))
        if num == False:
            return  num_list
        else:
            num_list.append(num)


def sumatoria():
    numbers = obtener_numeros()
    total = 0
    for i in numbers:
        total += i
    return total

#def multiplicacion():
print(sumatoria())