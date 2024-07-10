import csv
import json

def leer_datos(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        datos = csv.reader(file)
        datos = list(datos)
        datos.pop(0)
    return datos

interacciones = leer_datos('interacciones.csv')
usuarios = leer_datos('usuarios.csv')

def contar_likes(data, user):
    contador_likes = 0
    for i in data:
        if i[0] == user:
            if i[2] == 'like':
                contador_likes += 1
    return contador_likes

def contar_comentarios(data, user):
    contador_comentarios = 0
    for i in data:
        if i[0] == user:
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

def top_usuarios(interacciones):
    usuarios = []
    interacciones_usuarios = []
    for i in interacciones:
        if i[0] not in usuarios: usuarios.append(i[0])
    for i in usuarios:
        contador_interacciones = 0
        for j in interacciones:
            if i == j[0]: contador_interacciones += 1
        interacciones_usuarios.append([i, contador_interacciones])
    interacciones_usuarios = sorted(interacciones_usuarios, key=lambda e: e[1], reverse=True)
    top_tres_usuarios = interacciones_usuarios[0:3]
    return top_tres_usuarios

def es_top_usuario(interacciones, user):
    for i in interacciones:
        if user in i[0]: return True
    return False


def escribir_reporte(usuarios):
    dic_usuarios = []
    for i in usuarios:
        user = {
            'nombre' : i[1],
            'id' : i[0],
            'edad' : calcular_edad(usuarios, i[1]),
            'total_likes' : contar_likes(interacciones, i[0]),
            'total_comments' : contar_comentarios(interacciones, i[0]),
            'numero_interacciones' : total_interacciones(contar_likes(interacciones, i[0]), contar_comentarios(interacciones, i[0])),
            'es_top_usuario' : es_top_usuario(top_usuarios(interacciones), i[0] )
        }
        dic_usuarios.append(user)
    return dic_usuarios
 
reporte = escribir_reporte(usuarios)

with open('reporte_interacciones.json', 'w', newline='') as f:
    json.dump(reporte, f)

with open('reporte_interacciones.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id_usuario', 'nombre_usuario', 'edad', 'total_likes', 'total_comments', 'numero_interacciones', 'es_top_usuario'])
    for i in reporte:
        writer.writerow([i['id'], i['nombre'], i['edad'], i['total_likes'], i['total_comments'], i['numero_interacciones'], i['es_top_usuario']])
