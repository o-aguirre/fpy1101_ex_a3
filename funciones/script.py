import csv
import funciones as fn

data = []

with open('../actividad_3.3.3/alumnos_detallado.csv', 'r', encoding='utf-8') as f:
    file = csv.reader(f)
    file = list(file)
    for i in range(1, len(file)):
        data.append(file[i])

print(data)

