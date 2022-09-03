debito = 700
x = 1
divida = 0
while x <= 3:
    d = float(input(f'Sobre dívida informe o valor que você deseja pagar: '))
    divida+=d
    x+=1
print(f'No total de R${debito} você quitou {debito-d:6.2f}')