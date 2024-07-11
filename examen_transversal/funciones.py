def clasificar_sueldos(trabajadores):
    tier1 = []
    tier2 = []
    tier3 = []
    total_sueldos = 0
    for i in trabajadores:
        total_sueldos += i[1]
        if i[1] < 800000: tier3.append(i)
        if i[1] > 800000 and i[1] < 2000000: tier2.append(i)
        if i[1] > 2000000: tier1.append(i)       
    print(f'SUELDOS MENORES A $800.000      TOTAL: {len(tier3)}')
    for i in tier3:
        print(f'NOMBRE DE EMPLEADO: {i[0]}      SUELDO: {i[1]}')
    print(f'SUELDOS ENTRE $800.000 Y $2.000.000      TOTAL: {len(tier2)}')
    for i in tier2:
        print(f'NOMBRE DE EMPLEADO: {i[0]}      SUELDO: {i[1]}')
    print(f'SUELDOS MAYORES A $2.000.000        TOTAL: {len(tier1)}')
    for i in tier1:
        print(f'NOMBRE DE EMPLEADO: {i[0]}      SUELDO: {i[1]}')
    print(f'Total Sueldos: {total_sueldos}')


def sacar_mas_alto(sueldos):
    sueldos = sorted(sueldos, key=lambda e: e[1], reverse=True)
    mas_alto = sueldos[:1]
    return mas_alto

def sacar_mas_bajo(sueldos):
    sueldos = sorted(sueldos, key=lambda e: e[1])
    mas_bajo  = sueldos[:1]
    return mas_bajo
    
def sacar_promedio_sueldos(sueldos):
    total = 0
    for i in sueldos:
        total += i[1]
    return total / len(sueldos)

def medida_geometrica(sueldos):
    multiplicacion = 1
    for i in sueldos:
        multiplicacion *= i[1]
    return multiplicacion ** (1/10)

def estadisticas_sueldos(higher, lower, average, medida,):
    print(f'Sueldo mas alto: {higher[0]}')
    print(f'Sueldo mas bajo: {lower[0]}')
    print(f'Promedio sueldos: {average}')
    print(f'Medida geometrica: {medida}')

def reporte_de_sueldos(sueldos):
    sueldo = 0
    reporte_empleados = []
    print('NOMBRE EMPLEADO   SUELDO BASE   DESCUENTO SALUD   DESCUENTO AFP   SUELDO LIQUIDO')
    for i in sueldos:
        sueldo = i[1] - int(i[1] * 0.07) - int(i[1] * 0.12)
        print(f'{i[0]}        {i[1]}          {int(i[1] * 0.07)}          {int(i[1] * 0.12)}            {sueldo}')
        reporte_empleados.append([i[0],i[1],int(i[1] * 0.07),int(i[1] * 0.12),sueldo])
    return reporte_empleados

def salir():
    print('Finalizando programa...')
    print('Desarrollado por Onesimo Aguirre')
    print('RUT: 18.842.528-3')