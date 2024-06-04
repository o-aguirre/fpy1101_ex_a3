#Cree una lista y comience a almacenar nombres, cada vez que se agregue un nombre nuevo,
#el sistema preguntará si desea agregar otro nombre, deberá agregar nombres hasta que la respuesta sea 
#“no”, “No”, “nO” o “NO” (use funciones lower() y upper() ) .
#Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de caracteres.

names = []
shorter = ''

while True:
    opt = input('Deseas guardar un nombre? Si/No: ')
    opt.lower()
    if opt == 'si':
        names.append(input('Ingresa un nombre: '))
    if opt == 'no':
        for e in range(len(names) - 1):
            if len(names[e]) < len(names[e + 1]):
                shorter = names[e]
            else:
                shorter = names[e + 1]
        names.remove(shorter)
        break

print(names)
