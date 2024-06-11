#Creen un programa que permita almacenar nombres en una lista. El sistema debe preguntar si desean agregar otro nombre y seguir permitiendo la entrada de nombres
#hasta que la respuesta sea "no". Después de ingresar n nombres, eliminen el nombre con la menor cantidad de caracteres

names = []
opt = ''
larger = 0

while True:
    opt = input('Desea agregar un nombre? Si/No: ')
    if opt.lower() == 'si': names.append(input('Ingresa un nombre: '))
    elif opt.lower() == 'no': break

for i in range(len(names)):
    if larger:
        if len(larger) > len(names[i]):
            larger = i
        else: larger = i

names.pop(larger)
print(names)