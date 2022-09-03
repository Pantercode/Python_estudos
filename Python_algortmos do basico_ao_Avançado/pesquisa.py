lista = [1, 15, 19, 46, 460, 370]
p = int(input('Digite o número a pesquisar: '))
for cont in lista:
    if cont == p:
        print(f'O elemento {p} foi encontrado.')
        break
else:
    print('O elemento {p} não foi encontrado !!')