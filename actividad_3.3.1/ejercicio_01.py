tupla_nombres = ()

while True:
    name = input('Ingrese un nombre: ')
    tupla_nombres = set(tupla_nombres)
    tupla_nombres.add(name)
    if len(tupla_nombres) == 3:
        break
    

tupla_nombres = tuple(tupla_nombres)
shorter = ''

for i in tupla_nombres:
    if shorter:
        if len(i) < len(shorter):
            shorter = i
    else:
        shorter = i

print(tupla_nombres)
print(shorter)



#Otra manera
#tupla_nombres = ()

#while True:
    #name = input('Ingrese un nombre: ')
    #tupla_nombres += (name, )
    #tupla_nombres = set(tupla_nombres)
    #if len(tupla_nombres) == 3:
        #break
    #else:
        #tupla_nombres = tuple(tupla_nombres)
    
#print(tupla_nombres)