users = {
    'ramon':'donramon',
    'luis':'luchito'
}
option = 0

def menu():
    print('1. Inicio sesión')
    print('2. Registrar usuario')
    print('3. Eliminar usuario')
    print('4. Salir')
    
while True:
    menu()
    option = int(input())
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

    if option == 3:
        user = input('Ingresa usuario a eliminar: ')
        if user in users:
            users.pop(user)
        else:
            print('Usuario no encontrado')

    if option == 4:
        break
