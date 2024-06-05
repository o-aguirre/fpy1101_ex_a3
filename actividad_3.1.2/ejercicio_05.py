# Cree un sistema de ventas de supermercado en el cual se pueda agregar productos al carro de compras, las opciones del menú serán
#1. Agregar productos
#2. Ver canasta
#3. Ver total
#4. Salir
#En agregar productos deberá mostrar un menú con 5 productos y sus precios (creado por usted), cada vez que se seleccione un producto
#quedará agregado en la lista.
#Ver canasta, es mostrar todos los productos seleccionados.
#Ver total, es mostrar el total a pagar por el cliente.

precios_productos = {
    'aceite' : 1500,
    'leche' : 1100,
    'pañal' : 10000,
    'arroz' : 1700,
    'bebida' : 2500
}
carro_compra = []
total = 0

print('1. Agregar productos: ')
print('2. Ver canasta: ')
print('3. Ver total: ')
print('4. Salir: ')
opt = 0

while opt != 4:
    opt = int(input(''))
    if opt == 1:
        producto = input('Ingrese un poducto: ')
        if producto in precios_productos:
            carro_compra.append(producto)
            total += precios_productos[producto]

    if opt == 2:
        for e in carro_compra:
            print(f'{e} = {precios_productos[e]}')

    if opt == 3:
        print(f'Total: {total}')
   
print(f'Total compra: {total}')
