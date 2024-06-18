import csv

#Primera manera
"""
archivo_texto = open('prueba.txt', 'a', encoding='utf-8')

#metodo 'w'
frase = 'text\nprueba con ñ'
archivo_texto.write(frase)
archivo_texto.close()

#leer archivos
texto = archivo_texto.readlines()

#escribir en archivos
archivo_texto.write('\nsiguiente linea')

#cerrar archivos
archivo_texto.close()
"""

#otra manera
"""
with open('prueba.txt', 'r', encoding='utf-8') as archivos:
    lineas = archivos.readlines()
    print(lineas)

for i in lineas:
    print(i.replace('\n', ''))
"""

"""
with open('datos.csv', 'w', encoding='utf-8', newline='') as archivo:
    escribir_csv = csv.writer(archivo)
    escribir_csv.writerows([
        ['nombre', 'apellido', 'nota1', 'nota2', 'nota3', 'asistencia'],
        ['Juan', 'Perez', '6.0', '4.0', '2.5', '90'],
        ['Jose', 'Perez', '6.0', '4.0', '2.5', '90'],
        ['Maria', 'Perez', '6.0', '4.0', '2.5', '90'],
        ['Carla', 'Perez', '6.0', '4.0', '2.5', '90'] 
        ])
"""

lista_de_datos = []

with open('datos.csv', 'r', encoding='utf-8', newline='') as archivo:
    lista_de_datos = csv.reader(archivo)

    for fila in lista_de_datos:
        print(fila)
