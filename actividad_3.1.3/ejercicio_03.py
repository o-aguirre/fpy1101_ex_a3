bus = []
asiento = 1

for x in range(10):
    fila_x = []
    bus.append(fila_x)
    for y in range(4):
        fila_x.append(asiento)
        asiento += 1

for e in range(len(bus)):
    print(bus[e])

reserva = int(input('Escoja un asiento: '))
for e in bus:
    for j in e:
        if reserva == j:
            e[j] == 'x'
