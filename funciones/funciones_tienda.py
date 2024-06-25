def agregar_productos(new_product, list_product):
    sku_product = new_product['sku']
    if sku_product in list_product['sku']:
        print('SKU ya existente')
        return list_product
    else:
        print('Agregado correctamente')
        return list_product.append(new_product)

def eliminar_productos():
    return

def actualizar_productos():
    return