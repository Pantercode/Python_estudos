
categoria = int(input('Digite a categoria escolhida[1 a 5]: '))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print('Categoria inválida,digite um valor de 1 a 5!')
print(f'O preço do produto e RS{preco:6.2f}')
