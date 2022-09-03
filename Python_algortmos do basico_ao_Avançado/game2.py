print('Bem vindo!')
achou = 0
while achou != 5:
    g = input('Adivinhe o número: ')
    achou = int(g)
    if achou == 5:
        print('Venceu')
    else:
        if achou > 5:
            print('Você digitou um a valor muito acima!')
        else:
            print('Você digitou um valor muito abaixo!')
        print('Fim de jogo!')

