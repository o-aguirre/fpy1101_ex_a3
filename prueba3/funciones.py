#Trabajador con mejor sueldo
def mejor_pagado(data):
    mejor_sueldo = 0
    for i in data:
        mejor_sueldo_trabajador = []
        try:
            sueldo = int(i['sueldo'])
        except:
            continue
        if sueldo > mejor_sueldo:
            trabajador = {
                'nombre' : i['nombre'],
                'apellido' : i['apellido'],
                'sueldo' : sueldo,
                'anio' : i['anio']
            }
            mejor_sueldo_trabajador.append(trabajador)
    print(f'El mejor trabajador {mejor_sueldo_trabajador[0]['nombre']} {mejor_sueldo_trabajador[0]['apellido']}')
    print(f'tiene un sueldo de {mejor_sueldo_trabajador[0]['sueldo']} en el año {mejor_sueldo_trabajador[0]['anio']}')

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

#Obtenemos los mejores sueldos por cargo en 2022
""" def mejores_2022(data):
    mejores_pagados = []
    sueldo_ingeniero = 0
    sueldo_analista = 0
    sueldo_tecnico = 0
    sueldo_gerente = 0
    sueldo_contador = 0
    sueldo_desarrollador = 0
    sueldo_jefe_proyectos = 0
    for i in data:
        if i['cargo'] == 'Ingeniero':

        if i['cargo'] == 'Analista':
        if i['cargo'] == 'Técnico':
        if i['cargo'] == 'Gerente':
        if i['cargo'] == 'Contador':
        if i['cargo'] == 'Desarrollador':
        if i['cargo'] == 'Jefe de Proyectos': """

        

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
    

        