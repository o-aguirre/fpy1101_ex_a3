import csv

lista_datos = []
total_asistencia = 0
cont = 0

with open('estudiantes.csv', 'r', encoding='utf-8', newline='') as archivo:
    lista_datos = csv.reader(archivo)

    #Promedio asistencia
    for fila in lista_datos:
        try:
            total_asistencia += int(fila[6])
            cont += 1
        except:
            print('err')   
    
print(f'El promedio de asistencia: {total_asistencia / cont}')

