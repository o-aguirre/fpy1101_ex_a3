import funciones as fn
import random
import csv

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','MiguelSSSánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']

def asignar_sueldo(trabajadores):
    trabajadores_sueldos = []
    for i in trabajadores:
        sueldo = random.randint(300000, 2500000)
        trabajadores_sueldos.append([i, sueldo])
    return trabajadores_sueldos


sueldos_trabajadores = None


print('INGRESA EL NUMERO CON LA OPCION QUE DESEAS')
print('1. INGRESA SUELDOS ALEATORIOS')
while True:
    opt = input()
    if opt == '1' : 
        sueldos_trabajadores = asignar_sueldo(trabajadores)
        sueldo_mas_alto = fn.sacar_mas_alto(sueldos_trabajadores)
        sueldo_mas_bajo = fn.sacar_mas_bajo(sueldos_trabajadores)
        promedio_sueldos = fn.sacar_promedio_sueldos(sueldos_trabajadores)
        medida_geometrica = fn.medida_geometrica(sueldos_trabajadores)
        break
    else:
        print('Debes ingresar uno para generar sueldos')

while True:
    print('2. CLASIFICAR SUELDOS')
    print('3. VER ESTADISTICAS')
    print('4. REPORTE DE SUELDOS')
    print('5. SALIR DEL PROGRAMA')
    opt = input()
    if opt == '2' : fn.clasificar_sueldos(sueldos_trabajadores)
    if opt == '3' : fn.estadisticas_sueldos(sueldo_mas_alto, sueldo_mas_bajo, promedio_sueldos, medida_geometrica)
    if opt == '4' : reporte_empleados = fn.reporte_de_sueldos(sueldos_trabajadores)
    if opt == '5' :
        fn.salir()
        break

#reporte_empleados = fn.reporte_de_sueldos(sueldos_trabajadores)
with open('datos_sueldos.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['nombre_emplado','sueldo_base','dsc_salud','dsc_afp','sueldo_liq'])
    for i in reporte_empleados:
        writer.writerow(i)