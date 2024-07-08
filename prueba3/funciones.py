import json
#Trabajador con mejor sueldo
def mejor_pagado(data):
    mejor_sueldo = 0
    for i in data:
        mejor_sueldo_trabajador = []
        try:
            sueldo = int(i['sueldo'])
            if sueldo > mejor_sueldo:
                trabajador = {
                    'nombre' : i['nombre'],
                    'apellido' : i['apellido'],
                    'sueldo' : sueldo,
                    'anio' : i['anio']
                }
        except:
            continue
    mejor_sueldo_trabajador.append(trabajador)
    
    print(f'El mejor trabajador {mejor_sueldo_trabajador[0]['nombre']} {mejor_sueldo_trabajador[0]['apellido']}')
    print(f'tiene un sueldo de {mejor_sueldo_trabajador[0]['sueldo']} en el año {mejor_sueldo_trabajador[0]['anio']}')
    with open(mejor_sueldo_trabajador[0]['nombre']+mejor_sueldo_trabajador[0]['apellido']+'.json', 'w', encoding='utf-8') as file:
        json.dump(mejor_sueldo_trabajador, file)
    return mejor_sueldo_trabajador

#Obtenemos todos los trabajadores de 2022
def obtener_trabajadores_2022(data):
    trabajadores_2022 = []
    for i in data:
        if i['anio'] == '2022':
            trabajador = {
                'nombre' : i['nombre'],
                'apellido' : i['apellido'],
                'cargo' : i['cargo'],
                'sueldo' : i['sueldo'],
                'anio' : i['anio']
            }
            trabajadores_2022.append(trabajador)
    return trabajadores_2022

def obtener_cargo(datos):
    cargos = []
    for i in datos:
        if i['cargo'] not in cargos and i['cargo'] != 'Cargo':
            cargos.append(i['cargo'])
    return cargos

def mejores_pagados_2022(anio, cargo):
    trabajadores = []
    for i in cargo:
        sueldo_mas_alto = 0
        trabajador = {}
        for j in anio:
            if i == j['cargo']:
                if int(j['sueldo']) > sueldo_mas_alto:
                    sueldo_mas_alto = int(j['sueldo'])
                    trabajador = {
                        'nombre' : j['nombre'],
                        'apellido' : j['apellido'],
                        'cargo' : j['cargo'],
                        'sueldo' : sueldo_mas_alto,
                    }
        trabajadores.append(trabajador)
    return trabajadores

def obtener_rut_usuario(data, rut):
    sueldo = []
    trabajador_dicc = {'2022': {}, '2023': {}}
    for i in data:
        if i['rut'] == rut:
            if i['anio'] == '2022':
                trabajador_dicc['2022'] = {
                        'nombre' : i['nombre'],
                        'apellido' : i['apellido'],
                        'rut' : i['rut'],
                        'cargo' : i['cargo'],              
                }
                sueldo.append(i['sueldo'])
                trabajador_dicc['2022']['sueldo'] = sueldo
   
            if i['anio'] == '2023':
                trabajador_dicc['2023'] = {
                        'nombre' : i['nombre'],
                        'apellido' : i['apellido'],
                        'rut' : i['rut'],
                        'cargo' : i['cargo'],
                    }
                sueldo.append(i['sueldo'])
                trabajador_dicc['2023']['sueldo'] = sueldo

    return trabajador_dicc
    

        