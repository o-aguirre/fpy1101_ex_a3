names = []
second_names = []

for i in range(3):
    names.append(input('Ingresa un nombre: '))
    second_names.append(input('Ingresa un apellido: '))

for e in range(len(names) - 1):
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names[i + 1], names[i]

for e in range(len(second_names) - 1):
    for i in range(len(second_names) - 1):
        if second_names[i] > second_names[i + 1]:
            second_names[i], second_names[i + 1] = second_names[i + 1], second_names[i]

print(names, second_names)