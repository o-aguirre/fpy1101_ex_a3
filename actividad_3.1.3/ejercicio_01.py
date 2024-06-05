import random

matriz = []

for x in range(3):
    lista_x = []
    matriz.append(lista_x)
    for y in range(4):
        lista_y = random.randint(1, 4)
        lista_x.append(lista_y)

print(matriz)
