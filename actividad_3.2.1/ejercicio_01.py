import random

matriz_3D = []

for x in range(3):
    lista_ = []
    matriz_3D.append(lista_)
    for y in range(4):
        lista = []
        lista_.append(lista)
        for e in range(4):
            elemento = random.randint(1, 3)
            lista.append(elemento)

print(matriz_3D)