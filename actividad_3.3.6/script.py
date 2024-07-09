import csv

def leer_datos(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        datos = csv.reader(file)
        datos = list(datos)
        datos.pop(0)
    return datos

interacciones = leer_datos('interacciones.csv')
usuarios = leer_datos('usuarios.csv')

#Terminar
def contar_likes(data, user):
    contador_likes = 0
    for i in data:
        if i[1] == user:
            if
            contador_likes += 1
    return contador_likes

def contar_comentarios(data):
    contador_comentarios = 0
    for i in data:
        if i[2] == 'comment':
            contador_comentarios += 1
    return contador_comentarios

def total_interacciones(likes, comments):
    return likes + comments

def calcular_edad(data, user):
    edad = ''
    for i in data:
        if user == i[1]:
            edad = i[2]
            edad = int(edad[:4])
    return 2024 - edad  

def ordenar(lista):
    return lista[1]

def mas_viciosos(interacciones, usuarios):
    interacciones_usuarios = []
    for i in usuarios:
        contador_interacciones = 0
        for j in interacciones:
            if i[0] == j[0]:
                contador_interacciones += 1
        interacciones_usuarios.append([i[1], contador_interacciones])   
    interacciones_usuarios.sort(key=ordenar)

    usuarios_mas_activos = interacciones_usuarios[-3:]
    print(usuarios_mas_activos)

def to_diccionario(usuarios):
    dic_usuarios = []
    for i in usuarios:
        user = {
            'id' : i[1],
            'edad' : calcular_edad(usuarios, i[1]),
            #terminar
            'total_likes' : contar_likes(interacciones),
            'total_comments' : contar_comentarios(interacciones),
            'numero_interacciones' : total_interacciones(contar_likes(interacciones), contar_comentarios(interacciones))
        }
        dic_usuarios.append(user)
    print(dic_usuarios)
 
#def escribir_reporte()
    

#print(contar_likes(interacciones))
#print(contar_comentarios(interacciones))
#print(total_interacciones(contar_likes(interacciones), contar_comentarios(interacciones)))
#calcular_edad(obtener_edad(usuarios))
#mas_viciosos(interacciones, usuarios)

to_diccionario(usuarios)
