import json
lista_notas = []

with open('notas.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)
    print(datos, type(datos))

