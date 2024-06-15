import csv
lista_datos = []
total_asistencia = 0
cont = 0

with open('estudiantes.csv', 'r', encoding='utf-8', newline='') as archivo:
    lista_datos = csv.reader(archivo)

    for fila in lista_datos:
        try:
            total_asistencia += int(fila[6])
            print(total_asistencia)
        except:
            print('err')
        cont += 1
        #total_asistencia += nota

    
print(total_asistencia / cont)

#Revisar promedio asstencia
#Promedio de notas por alumno y mostrar la mas alta