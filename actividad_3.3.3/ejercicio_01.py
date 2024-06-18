import csv

#lista de datos recibidos
lista_datos = []
new_lista_datos = []

#lista que recibe diccionario
lista_datos_diccionario = []

with open('alumnos_detallado.csv', 'r', encoding='utf-8') as file:
    datos = csv.reader(file)
    lista_datos = list(datos)

    for i in range(1, len(lista_datos)):
        new_lista_datos.append(lista_datos[i])

for i in new_lista_datos:
    diccionario_datos = {}
    diccionario_datos['rut'] = i[0]
    diccionario_datos['nombre'] = i[1]
    diccionario_datos['apellido'] = i[2]
    lista_datos_diccionario.append(diccionario_datos)

print(lista_datos_diccionario)

    

