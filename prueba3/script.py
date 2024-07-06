import csv
import json
import funciones as fn

with open('sueldos_1.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file)
    data = list(data)

data_sueldos = []
for i in data:
    sueldo_persona = {
        'nombre' : i[0],
        'apellido' : i[1],
        'edad' : i[2],
        'rut' : i[3],
        'afp' : i[4],
        'cargo' : i[5],
        'antiguedad' : i[6],
        'sueldo' : i[7],
        'mes' : i[8],
        'anio' : i[9],
        'genero' : i[10],
    }
    data_sueldos.append(sueldo_persona)

while True:
    print('1. Mejor pagado')
    print('2. Mejores sueldos 2022 por cargo')
    print('3. Buscar trabajador por RUT')
    opt = int(input())
    if opt == 1:
        fn.mejor_pagado(data_sueldos)
        with open('mejor_pagado.json', 'w') as file:
            archivo = json.dump(fn.mejor_pagado(data_sueldos), file)

    if opt == 2:
        print(fn.mejores_2022(data_sueldos))

    if opt == 3:
        rut = input('Ingrese rut usuario (formato xxxxxxx-x): ')
        fn.obtener_rut_usuario(data_sueldos, rut)
        with open('usuaro_rut.json', 'w') as file:
            archivo = json.dump(fn.obtener_rut_usuario(data_sueldos, rut), file)
    if opt == 4:
        break