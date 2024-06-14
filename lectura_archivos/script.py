#Primera manera
"""
archivo_texto = open('prueba.txt', 'a', encoding='utf-8')

#metodo 'w'
frase = 'text\nprueba con ñ'
archivo_texto.write(frase)
archivo_texto.close()

#leer archivos
texto = archivo_texto.readlines()

#escribir en archivos
archivo_texto.write('\nsiguiente linea')

#cerrar archivos
archivo_texto.close()
"""

#otra manera
with open('prueba.txt', 'r', encoding='utf-8') as archivos:
    lineas = archivos.readlines()
    print(lineas)

for i in lineas:
    print(i.replace('\n', ''))