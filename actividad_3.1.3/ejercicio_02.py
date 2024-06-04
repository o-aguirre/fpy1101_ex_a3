import random
arreglo = []
colors_list = ['amarillo', 'rojo', 'naranja', 'verde', 'blanco']

for x in range(3):
    x_list = []
    arreglo.append(x_list)
    for y in range(3):
        y_list = []
        x_list.append(y_list)
        for z in range(3):
            color = random.randint(0, 4)
            y_list.append(colors_list[color])

print(arreglo)