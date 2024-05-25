names_list = []
largerst = ''

for name in range(3):
    name = input('Ingresa un nombre: ')
    names_list.append(name)

for larger in range(len(names_list)):
    if len(names_list[larger]) > len(largerst):
        largerst = names_list[larger]

print(largerst)