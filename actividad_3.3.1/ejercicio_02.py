#Al menos debe tener 4 nombres con sus datos y estos deben ingresar por teclado
#Crear agenda telefonica donde la estructura del diccionario debe ser la siguiente

guia_telefono = {}

for i in range(2):
    nombre = input('Ingrese un nombre: ')
    telefono = dict(telefono = input('Ingrese telefono: '))
    email = dict(email = input('Ingrese email: '))
    direccion = dict(direccion =  input('Ingrese direccion: '))
    estado = dict(estado =  bool(input('Ingrese estado: ')))
    guia_telefono[nombre] = telefono
    guia_telefono[nombre] = email
    guia_telefono[nombre] = direccion
    guia_telefono[nombre] = estado

print(guia_telefono)