telefone = int(input('Informe os minutos que você gastou'))

if telefone <= 200:
    telefone = telefone +(telefone*0.20)
    print(f'Sua fatura está em um valor de {telefone:6.2f}')
    if telefone > 200 or telefone == 400:
        telefone = telefone + (telefone * 0.18)
        print(f'Sua fatura está em um valor de {telefone:6.2f}')
    else:
        telefone = telefone + (telefone * 0.15)
        print(f'Sua fatura está em um valor de {telefone:6.2f}')