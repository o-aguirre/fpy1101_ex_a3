#Crear una aplicación en donde pueda tener las siguientes opciones:
#- Sumar números.
#- Multiplicar números.
#- Cantidad de números pares e impares.
#- Obtener promedio de los números ingresados.
#- Obtener la suma de los factoriales de cada número

def obtener_numeros():
    num_list = []
    while True:
        try:
            num = int(input('Ingresa numero: '))
            num_list.append(num)
        except:
            return num_list

def sumatoria(numeros):
    total = 0
    for i in numeros:
        total += i
    return print(total)

def multiplicacion(numeros):
    total = 1
    for i in numeros:
        total *= i
    return print(total)

def par_impar(numeros):
    par = 0
    impar = 0
    for i in numeros:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
    return print(f'Total pares: {par}, total impares: {impar}')

def promedio(numeros):
    contador = 0
    total = 0
    for i in numeros:
        total += i
        contador += 1
    return print(f'Promedio : {total / contador}')

def factorial(numeros):
    total_suma = 0
    for i in numeros:
        total_multiplicacion = 1
        for j in range(1, i + 1):
            total_multiplicacion *= j
        total_suma += total_multiplicacion
    print(total_suma)

numeros = obtener_numeros()

while True:
    print('Ingrese una opcion')
    print('1. Sumar')
    print('2. Multiplicar')
    print('3. Cantidad de numeros pares e impares')
    print('4. Obtener promedio de numeros ingresados')
    print('5. Suma de los factoriales')
    try:    
        opt = int(input())
    except:
        break

    if opt == 1: sumatoria(numeros)
    if opt == 2: multiplicacion(numeros)
    if opt == 3: par_impar(numeros)
    if opt == 4: promedio(numeros)
    if opt == 5: factorial(numeros)
