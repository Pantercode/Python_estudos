menu = 0
while menu <= 0:
    n1 = int(input('Informe um operando: '))
    n2 = int(input('Informe outro operando: '))
    print('Caso queira sair do programa aperte 0')

    menu = int(input("""                     
    [1] Adição
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [5] Resto da divisão
    [6] Divisão de inteiros: """))

    if menu == 1:
        operacao = n1 + n2
    elif menu == 2:
        operacao =n1 - n2
    elif menu == 3:
        operacao = n1 * n2
    elif menu == 4:
        operacao = n1 / n2
    elif menu == 5:
        operacao =n1 % n2
    elif menu == 6:
        operacao = n1 // n2

print(f'O resultado solicitada é {operacao}.')
