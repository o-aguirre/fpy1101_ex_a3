import random

matriz_3D = []

for x in range(4):
    lista = []
    for y in range(4):
        elemento = random.randint(1, 10)
        matriz_3D.append(elemento)
    

print(matriz_3D)