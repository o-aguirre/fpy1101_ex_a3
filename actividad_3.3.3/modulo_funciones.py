
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

#Sacamos un promedio de datos pasados por parámtro
def promedio_asignatura(datos, asignatura):
    promedio_asignatura = 0
    cont = 0
    for i in datos:
        if i['asignatura'] == asignatura:
            try:
                promedio_asignatura += int(i['asistencia'])
                cont += 1
            except:
                continue
    return promedio_asignatura / cont

#Usando funcion para promediar, calculamos promedio de cada asignatura
def mejor_asistencia(datos):
    for i in datos:
        if i['curso'] == 'primer anio':
            promedio_intro = [promedio_asignatura(datos, 'Introduccion al Cloud Computing'), 'Introduccion al Cloud Computing']
            promedio_fundamentos = [promedio_asignatura(datos, 'Fundamentos de Programacion'), 'Fundamentos de Programacion']
            promedio_innovacion = [promedio_asignatura(datos, 'Innovacion'), 'Innovacion']
        if i['curso'] == 'segundo anio':
            promedio_inte_plataform = [promedio_asignatura(datos, 'Integraccion de plataformas'), 'Integraccion de plataformas']
            promedio_cal_integral = [promedio_asignatura(datos, 'calculo integral'), 'calculo integral']
            promedio_alg_lineal = [promedio_asignatura(datos, 'algebra lineal'), 'algebra lineal']
        if i['curso'] == 'tercer anio':
            promedio_estruc_datos = [promedio_asignatura(datos, 'Estructura de datos'), 'Estructura de datos']
            promedio_automatas = [promedio_asignatura(datos, 'Automatas'), 'Automatas']
            promedio_prog_web = [promedio_asignatura(datos, 'programacion web'), 'programacion web']
        if i['curso'] == 'cuarto anio':
            promedio_simulacion = [promedio_asignatura(datos, 'simulacion'), 'simulacion']
            promedio_base_datos = [promedio_asignatura(datos, 'Base de datos aplicada'), 'Base de datos aplicada']
            promedio_redes = [promedio_asignatura(datos, 'Redes y comunicaciones'), 'Redes y comunicaciones']
        if i['curso'] == 'quinto anio':
            promedio_electromagnetismo = [promedio_asignatura(datos, 'Electromagnetismo'), 'Electromagnetismo']
            promedio_int_negocio = [promedio_asignatura(datos, 'Inteligencia de negocio'), 'Inteligencia de negocio']
            promedio_bigdata = [promedio_asignatura(datos, 'big data'), 'big data']
            promedio_min_datos = [promedio_asignatura(datos, 'mineria de datos'), 'mineria de datos']
        if i['curso'] == 'sexto anio':
            promedio_tesis = [promedio_asignatura(datos, 'tesis'), 'tesis']
            promedio_practica = [promedio_asignatura(datos, 'practica'), 'practica']
    #print(promedio_intro, promedio_fundamentos, promedio_innovacion)
    primer_anio = promedio_mayor(promedio_intro, promedio_fundamentos, promedio_innovacion)
    segundo_anio = promedio_mayor(promedio_inte_plataform, promedio_cal_integral, promedio_alg_lineal)
    tercer_anio = promedio_mayor(promedio_estruc_datos, promedio_automatas, promedio_prog_web)
    cuarto_anio = promedio_mayor(promedio_simulacion, promedio_base_datos, promedio_redes)
    quinto_anio = promedio_mayor(promedio_electromagnetismo, promedio_int_negocio, promedio_bigdata, promedio_min_datos)
    sexto_anio = promedio_mayor(promedio_tesis, promedio_practica)
    print(f'Asignatura con mejor asistencia en primer año: {primer_anio[0][1]} con un promedio de {primer_anio[0][0]}%')
    print(f'Asignatura con mejor asistencia en segundo año: {segundo_anio[0][1]} con un promedio de {segundo_anio[0][0]}%')
    print(f'Asignatura con mejor asistencia en tercer año: {tercer_anio[0][1]} con un promedio de {tercer_anio[0][0]}%')
    print(f'Asignatura con mejor asistencia en cuarto año: {cuarto_anio[0][1]} con un promedio de {cuarto_anio[0][0]}%')
    print(f'Asignatura con mejor asistencia en quinto año: {quinto_anio[0][1]} con un promedio de {quinto_anio[0][0]}%')
    print(f'Asignatura con mejor asistencia en sexto año: {sexto_anio[0][1]} con un promedio de {sexto_anio[0][0]}%')



def promedio_mayor(num1, num2, num3=[0], num4=[0]):
    mayor = []
    if num1[0] > num2[0] and num1[0] > num3[0] and num1[0] > num4[0]: mayor.append(num1)
    if num2[0] > num1[0] and num2[0] > num3[0] and num1[0] > num4[0]: mayor.append(num2)
    if num3[0] > num1[0] and num3[0] > num2[0] and num1[0] > num4[0]: mayor.append(num3)
    if num4[0] > num1[0] and num4[0] > num2[0] and num4[0] > num3[0]: mayor.append(num4)
    return mayor

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
        mejor_asistencia(datos)