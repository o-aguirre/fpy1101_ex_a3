#importar modulo csv
import csv

#creamos archivo y escribimos en el
"""
with open('notes.csv', 'w', encoding='utf-8', newline='') as archivo:
    new_file = csv.writer(archivo)
    new_file.writerows([
        ['Alumno/a','Primera evaluación','Segunda evaluación','Tercera evaluación'],
        ['alumno A','9.5','8','8'],
        ['alumno B','6.5','6','4.5'],
        ['alumno C','3','5.5','6'],
        ['alumno D','5.5','4.5','6'],
        ['alumno E','10','9','9'],
        ['alumno F','4','6','6.5'],
        ['alumno G','3','2.5','5'],
        ['alumno H','4','4.5','5'],
        ['alumno I','3','3.5','5'],
        ['alumno J','5.5','6','7'],
        ['alumno K','6.5','7','3.5'],
        ['alumno L','4.5','4','3.5'],
        ['alumno M','7.5','8','7.5'],
        ['alumno N','7','6.5','6'],
        ['alumno O','3','2.5','6'],
        ['alumno P','6.5','5','6'],
        ['alumno Q','2.5','4','4'],
    ])
"""
lista_datos = []
promedios = []
promedio = 0

with open('notes.csv', 'r', encoding='utf-8', newline='') as archivo:
    datos = csv.reader(archivo, delimiter=',')
    lista_datos = list(datos)
    for i in range(1, len(lista_datos)):
        promedios.append(lista_datos[i][1])
    
for i in promedios:
    promedio += float(i)

print(f'promedio = {promedio / len(promedios)}')