#Crear un menu en donde pueda agregar, actualizar, eliminar productos de una tienda
import funciones_tienda as fn

productos = [
    {
        'nombre_producto' : 'Coca Cola',
        'precio' : 1990,
        'cantidad' : 60,
        'sku' : 1
    },
    {
        'nombre_producto' : 'Galletas',
        'precio' : 600,
        'cantidad' : 400,
        'sku' : 2
    },
    {
        'nombre_producto' : 'Papas fritas',
        'precio' : 300,
        'cantidad' : 1000,
        'sku' : 3
    },
]

salir = False

while not salir:
    print('1.-Agregar producto')
    print('2.-Agregar producto')
    print('3.-Agregar producto')
    print('4.-Agregar producto')
    op = int(input())
    if op == 1:
        nuevo_producto = {
            'nombre_producto' : input('Ingrese nombre producto'),
            'precio' : input('Ingrese precio producto'),
            'cantidad' : input('Ingrese cantidad producto'),
            'sku' : input('Ingrese sku producto'),
        }
        productos = fn.agregar_productos(nuevo_producto, productos)