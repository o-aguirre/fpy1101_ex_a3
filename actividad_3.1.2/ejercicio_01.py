names_list = []
larger = ''

for i in range(3):
    name = input('Ingresa un nombre: ')
    names_list.append(name)

for e in range(3):
    if len(names_list[e]) > len(larger):
        larger = names_list[e]
    
print(larger)