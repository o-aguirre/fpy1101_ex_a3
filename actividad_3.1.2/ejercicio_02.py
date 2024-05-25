names_list = []
last_names_list = []

for i in range(3):
    name = input('Ingresa un nombre: ')
    last_name = input('Ingresa un apellido: ')
    names_list.append(name)
    last_names_list.append(last_name)

for i in range(3):
    print(f'Nombre: {names_list[i]} Apellido: {last_names_list[i]}')