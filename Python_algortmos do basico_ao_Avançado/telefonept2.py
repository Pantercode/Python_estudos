telefone = int(input('Informe os minutos que você gastou: '))
if telefone <= 200:
    preco = 0.20
else:
    if telefone < 400:
        preco = 0.18
    else:
        preco = 0.15
print(f'Sua fatura está em no valor de {telefone*preco:6.2f}')