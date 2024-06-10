#Al menos debe tener 4 nombres con sus datos y estos deben ingresar por teclado
#Crear agenda telefonica donde la estructura del diccionario debe ser la siguiente

guia_telefono = {}

for i in range(2):
    nombre = input('Ingrese un nombre: ')
    telefono = input('Ingrese telefono: ')
    email = input('Ingrese email: ')
    direccion = input('Ingrese direccion: ')
    estado = bool(input('Ingrese estado: '))
    guia_telefono[nombre] = {
        "telefono" : telefono,
        'email' : email,
        'direccion' : direccion,
        'estado' : estado,
    }
    

print(guia_telefono)