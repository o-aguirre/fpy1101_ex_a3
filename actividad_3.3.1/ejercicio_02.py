import csv

promedio_alumno = 0
nota_mas_alta = 0
alumno = []

with open('estudiantes.csv', 'r', encoding='utf-8', newline='') as archivo:
    lista_datos = csv.reader(archivo)
    for fila in lista_datos:
        try:
            promedio_alumno = (float(fila[3]) + float(fila[4]) + float(fila[5])) / 3
            if promedio_alumno > nota_mas_alta:
                nota_mas_alta = promedio_alumno
                alumno = fila
        except:
            print('err')

print(f'El promedio mas alto es: {nota_mas_alta}')
print(alumno)