#Crear una aplicaion que permita almacenar personas en diccionarios dentro de una lista
#Los datos deben ser ingresados mediante teclado teniendo la siguiente estructura:
#nombre, apellido, direccion, rut, genero, correo

lista_personas = []
cantidad_usuario = 2

for i in range(cantidad_usuario):
    datos_personas = {}
    datos_personas['nombre'] = input('Ingrese el nombre: ')
    datos_personas['direccion'] = input('Ingrese el direccion: ')
    datos_personas['rut'] = input('Ingrese el rut: ')
    datos_personas['correo'] = input('Ingrese el correo: ')
    lista_personas.append(datos_personas)

#print(lista_personas)

#Buscar nombre mas corto
shorter = ''
for lista in lista_personas:
    if shorter:
        if len(lista['nombre']) < len(shorter):
            shorter = lista['nombre']
    else: shorter = lista['nombre']
print(shorter)