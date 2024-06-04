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