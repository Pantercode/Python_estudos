while True:
    codigo = int(input('Informe um código e para finalizar digite 0: '))
    if codigo == 1:
        quantidade = int(input('Informe a quantidade: '))
        preco = 0.50
    elif codigo == 2:
        quantidade = int(input('Informe a quantidade: '))
        preco = 1.10
    elif codigo == 3:
        quantidade = int(input('Informe a quantidade: '))
        preco = 4.0
    elif codigo == 4:
        quantidade = int(input('Informe a quantidade: '))
        preco = 1.55
    elif codigo == 5:
        quantidade = int(input('Informe a quantidade: '))
        preco = 7.00
    elif codigo == 6:
        quantidade = int(input('Informe a quantidade: '))
        preco = 10.90
    elif codigo == 7:
        quantidade = int(input('Informe a quantidade: '))
        preco = 8.15
    elif codigo == 8:
        quantidade = int(input('Informe a quantidade: '))
        preco = 10.90
    elif codigo == 9:
        quantidade = int(input('Informe a quantidade: '))
        preco = 8.00
    elif codigo == 0:
        break
    else:
        print('Codigo inválido')
print(f'O total da compras resultou o valor de R${quantidade*preco}')