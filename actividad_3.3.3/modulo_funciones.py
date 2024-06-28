
#Funcion que calcula el promedio mas alto segun asignatura dada
def sacar_promedio (datos, asignatura):
    promedio_alumno = 0
    promedio_mas_alto = 0
    alumno_mejor_promedio = {}
    for i in datos:
        if i['asignatura'] == asignatura:
            promedio_alumno = (float(i['notas']['nota1']) + float(i['notas']['nota1']) + float(i['notas']['nota1'])) / 3
            if promedio_alumno > promedio_mas_alto:
                promedio_mas_alto = promedio_alumno
                alumno_mejor_promedio = {
                    'nombre' : i['nombre'],
                    'apellido' : i['apellido'],
                    'asignatura' : asignatura,
                    'promedio' : promedio_mas_alto,
                }
    print(alumno_mejor_promedio)

#Funcion que calcula los mejores promedio por año
def mejores_por_anio(datos, anio):
    alumnos = []
    promedio_mas_alto = 0
    alumno_mejor_promedio = {}
    
    #Obtenemos las notas por año
    for i in datos:
        alumno = []
        if i['curso'] == anio:
            alumno.append(i['nombre'])
            alumno.append(i['apellido'])
            alumno.append(i['curso'])
            alumno.append((float(i['notas']['nota1']) + float(i['notas']['nota2']) + float(i['notas']['nota3'])) / 3)
            alumnos.append(alumno)

    #Obtenemos promedio mas alto
    for i in alumnos:
        if i[3] > promedio_mas_alto:
            promedio_mas_alto = i[3]
            alumno_mejor_promedio['nombre'] = i[0]
            alumno_mejor_promedio['apellido'] = i[1]
            alumno_mejor_promedio['curso'] = i[2]
            alumno_mejor_promedio['promedio'] = i[3]
    print(alumno_mejor_promedio)

def promedio_mejor_asistencia(datos):
    mejor_asistencia = []
    promedio_asistencia = 0
    for i in datos:
        if i['curso'] == 'primer anio':
            if promedio('Introduccion al Cloud Computing', datos) > mejor_asistencia: 
                mejor_asistencia = promedio('Introduccion al Cloud Computing', datos)
            elif promedio('Fundamentos de Programacion', datos):
                mejor_asistencia = promedio('Fundamentos de Programacion', datos)

def promedio(asignatura, datos):
    total_promedio = 0
    contador = 0
    for i in datos:
        if i['asignatura'] == asignatura:
            total_promedio += int(i['asistencia'])
            contador += 1
    return total_promedio / contador

#Funcion imprime resultados
def imprimir(datos, opcion):
    if opcion == 1:
        sacar_promedio(datos, 'Introduccion al Cloud Computing')
        sacar_promedio(datos, 'Fundamentos de Programacion')
        sacar_promedio(datos, 'Innovacion')
        sacar_promedio(datos, 'Integraccion de plataformas')
        sacar_promedio(datos, 'calculo integral')
        sacar_promedio(datos, 'algebra lineal')
        sacar_promedio(datos, 'Estructura de datos')
        sacar_promedio(datos, 'Automatas')
        sacar_promedio(datos, 'programacion web')
        sacar_promedio(datos, 'simulacion')
        sacar_promedio(datos, 'Base de datos aplicada')
        sacar_promedio(datos, 'Redes y comunicaciones')
        sacar_promedio(datos, 'Electromagnetismo')
        sacar_promedio(datos, 'Inteligencia de negocio')
        sacar_promedio(datos, 'big data')
        sacar_promedio(datos, 'mineria de datos')
        sacar_promedio(datos, 'tesis')
        sacar_promedio(datos, 'practica')
    if opcion == 2:
        mejores_por_anio(datos, 'primer anio')
        mejores_por_anio(datos, 'segundo anio')
        mejores_por_anio(datos, 'tercer anio')
        mejores_por_anio(datos, 'cuarto anio')
        mejores_por_anio(datos, 'quinto anio')
        mejores_por_anio(datos, 'sexto anio')
    if opcion == 3:
        mejor_asistencia_anio(datos)
        