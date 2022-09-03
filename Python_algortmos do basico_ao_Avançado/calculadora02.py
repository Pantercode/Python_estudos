n1 = int(input('Escolha um numero de 1 a 10: '))
n2 = int(input('Escolha outro numero de 1 a 10: '))
menu =int(input(""" Qual operação deseja fazer 
    [1] Soma
    [2] Subtração
    [3] Divisão
    [4] Multiplicação
    Escolha o tipo de operação que deseja matemática:  """))
if menu == 1:
    operacao = n1 + n2
elif menu == 2:
    operacao = n1 - n2
elif menu == 3:
    operacao = n1 / n2
elif menu == 4:
    operacao = n1 * n2
else:
    print('Operação Inválida')
print(f'O resultado da expressão matemática solicitada resultou em:{operacao}')
