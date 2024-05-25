stock_5000 = 30
stock_2000 = 30
stock_1000 = 50

#intentar_nuevamente = True

while True:
    monto_a_retirar = int(input('Monto a retirar: '))
    stock_temporal_5000 = stock_5000
    stock_temporal_2000 = stock_2000
    stock_temporal_1000 = stock_1000

    if (monto_a_retirar > (stock_5000 * 5000 + stock_temporal_2000 * 2000 + stock_1000 * 1000)):
        print('No tengo ese stock')
    else:
        billetes_5000 = 0
        billetes_2000 = 0
        billetes_1000 = 0


        while monto_a_retirar >= 5000 and stock_temporal_5000 > 0:
            stock_5000 -= 1
            stock_temporal_5000 += 1
            monto_a_retirar -= 5000
        while monto_a_retirar >= 2000 and stock_temporal_2000 > 0:
            stock_2000 -= 1
            stock_temporal_2000 += 1
            monto_a_retirar -= 2000
        while monto_a_retirar >= 1000 and stock_temporal_1000 > 0:
            stock_1000 -= 1
            stock_temporal_1000 += 1
            monto_a_retirar -= 1000
        print('Monto: ', monto_a_retirar)
        print('Cantidad necesaria de 2000 ', billetes_5000)
        print('Cantidad necesaria de 5000 ', billetes_2000)
        print('Cantidad necesaria de 1000 ', billetes_1000)
        
        if (monto_a_retirar > 0):
            print('No puedo dar ese monto ', monto_a_retirar)
        else:
            stock_5000 = stock_temporal_5000 - billetes_5000
            stock_2000 = stock_temporal_2000 - billetes_2000
            stock_1000 = stock_temporal_1000 - billetes_1000
        print('Stock restante 5000: ', stock_5000)
        print('Stock restante 2000: ', stock_2000)
        print('Stock restante 1000: ', stock_1000)

        if (stock_5000 == 0 and stock_2000 == 0 and stock_1000 == 0):
            break
