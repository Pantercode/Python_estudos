from aleatorios import randint

secreto = randint(1, 10)

achou = 0
while achou != secreto:
    print('Bem vindo!')
    g = input('Adivinhe o número: ')
    achou = int(g)
    if achou == secreto:
        print('Venceu')
    else:
        if achou > secreto:
            print('Você digitou um a valor muito acima!')
        else:
            print('Você digitou um valor muito abaixo!')
        print('Fim de jogo!')
