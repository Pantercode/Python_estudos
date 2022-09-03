for g in range(0, 8):
    print('Bem vindo!')
    g = input('Adivinhe o número: ')
    achou = int(g)
    if achou == 5:
        print('Parabéns,voce acertou!!')
    elif achou < 5:
        print('UFa,Foi por pouco tente subir o valor do número')
    elif achou > 5:
        print('Foi por pouco tente descer o valor do número')
    else:
        print('Você perdeu!')
print('Fim do jogo!!')


