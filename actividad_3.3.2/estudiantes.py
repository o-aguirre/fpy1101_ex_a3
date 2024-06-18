import csv
import json

lista_datos = []
lista_datos_csv = []

#nueva lista sin encabezado
new_lista_datos = []
#lista de promedio de asistencia
lista_pomedio_asistencia = []
suma_total_asistencia = 0

#promedio notas alumnos
promedio_notas_alumno = 0
promedio_mas_alto = 0
alumno_mayor_promedio = []

with open('estudiantes.csv', 'r', encoding='utf-8', newline='') as file:
    datos = csv.reader(file)
    lista_datos_csv = list(datos)
    for i in range(1, len(lista_datos_csv)):
        new_lista_datos.append(lista_datos_csv[i])

    for i in new_lista_datos:
        diccionario_datos = {}
        diccionario_datos['nombre'] = i[0]
        diccionario_datos['notas'] = {}
        diccionario_datos['notas']['nota1'] = i[3]
        diccionario_datos['notas']['nota2'] = i[4]
        diccionario_datos['notas']['nota3'] = i[5]
        diccionario_datos['asistencia'] = i[6]
        lista_datos.append(diccionario_datos)

with open('estudiantes.json', 'w') as file:
    json_datos = json.dump(lista_datos, file)

with open('estudiantes.json', 'r', ) as file:
    datos = json.load(file)
    for i in datos:
        #asistencia promedio
        lista_pomedio_asistencia.append(i['asistencia'])
        suma_total_asistencia += int(i['asistencia'])
        #pomedio nota mas alta
        promedio_notas_alumno = float(i['notas']['nota1']) + float(i['notas']['nota2']) + float(i['notas']['nota3'])
        if promedio_notas_alumno > promedio_mas_alto:
            alumno_mayor_promedio = i


print(f'Promedio de asistencia = {suma_total_asistencia / len(lista_pomedio_asistencia)}')
print(alumno_mayor_promedio)