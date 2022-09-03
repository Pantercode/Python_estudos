while True:
    numero = int(input('Informe um número: '))
    if numero % 2 == 0:
        print(f'O numero {numero} não é  primo!')
    else:
        print(f'O numero {numero} é primo!')
        break