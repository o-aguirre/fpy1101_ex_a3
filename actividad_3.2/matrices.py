matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

#for i in matriz:
#    for e in i:
#        print(e)


lista_credenciales = []
for el in range(3):
    credenciales = []
    usuario = input('Ingrese un usuario: ')
    credenciales.append(usuario)
    password = input('Ingrese password: ')
    credenciales.append(password)
    lista_credenciales.append(credenciales)


for lista in range(len(lista_credenciales)):
    if lista_credenciales[lista][0] == 'juan':
        print('encntrado')