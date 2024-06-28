#Crear función que según una palabra, me retorne su tamaño. No se puede ocupar len() para este ejercicio

palabra = input('Ingresa una palabra: ')

def largo_palabra(word):
    contador = 0
    for i in word:
        contador += 1
    return contador

print(largo_palabra(palabra))