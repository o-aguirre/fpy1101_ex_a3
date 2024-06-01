users = {}
option = 0

def menu():
    print('1. Inicio sesión')
    print('2. Registrar usuario')
    print('3. Eliminar usuario')
    print('4. Salir')
    option = int(input())
    return option

while True:
    if option == 1:
        user = input('Ingrese usuario: ')
        password = input('Ingrese contraseña: ')
        if user in users:
            if users[user] == password:
                print('Sesión correcta')
            else:
                print('Contraseña incorrecta')
        else:
            print('Usuario no encontrado')

    if option == 2:
        users.update({input('Ingresa un usuario: '): input('Ingresa una contraseña: ')})

    option = int(input('Ingrese un opción'))

print(users)
