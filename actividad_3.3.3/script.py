#Transformar datos CSV a una lista de diccionarios
#Crear Menú que tengan las siguientes funcionalidades
#1.-Obtener el mejor alumno por asignatura
#2.-Obtener el mejor alumno por año
#3.-Obtener la asignatura de cada año con mejor asistencia
import csv
import modulo_funciones as f

#lista que recibe diccionario
diccionario_datos = []

with open('alumnos_detallado.csv', 'r', encoding='utf-8') as file:
    datos = csv.reader(file)
    datos = list(datos)

#Creacion diccionario
for i in datos:
    alumno = {
        'rut' : i[0],
        'nombre' : i[1],
        'apellido' : i[2],
        'curso' : i[3],
        'asignatura' : i[4],
        'notas' : {
            'nota1' : i[5],
            'nota2' : i[6],
            'nota3' : i[7]
        },
        'asistencia' : i[8]
    }
    diccionario_datos.append(alumno)

print('******************************************************************')
print('Informacion alumnos')
print('******************************************************************')

while True:
    print('\nEscoge una opcion para desplegar informacion')
    print('1. Obtener el mejor alumno por asignatura')
    print('2. Obtener el mejor alumno por año')
    print('3. Obtener la asignatura de cada año con mejor asistencia')
    print('4. Salir')
    try:
        opt = int(input())
    except:
        break
    if opt == 4:
        break
    else:
        f.imprimir(diccionario_datos, opt)

