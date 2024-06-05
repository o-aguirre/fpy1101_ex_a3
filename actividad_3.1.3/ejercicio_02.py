import random
arreglo = []
colors_list = ['amarillo', 'rojo', 'naranja', 'verde', 'blanco']
total_amarillo = 0
total_rojo = 0
total_naranja = 0
total_verde = 0
total_blanco = 0

for x in range(3):
    x_list = []
    arreglo.append(x_list)
    for y in range(3):
        y_list = []
        x_list.append(y_list)
        for z in range(3):
            color = random.randint(0, 4)
            if colors_list[color] == 'amarillo':
                total_amarillo += 1
            if colors_list[color] == 'rojo':
                total_rojo += 1
            if colors_list[color] == 'naranja':
                total_naranja += 1
            if colors_list[color] == 'verde':
                total_verde += 1
            if colors_list[color] == 'blanco':
                total_blanco += 1
            y_list.append(colors_list[color])

print(arreglo)
print(f'Total amarillo: {total_amarillo}')
print(f'Total rojo: {total_rojo}')
print(f'Total naranja: {total_naranja}')
print(f'Total verde: {total_verde}')
print(f'Total blanco: {total_blanco}')