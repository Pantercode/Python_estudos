categoria = int(input('Escolha a categoria [1 a 6]: '))
if categoria == 1:
    linhas_executadas = 1, 2, 3, 1, 9
else:
    if categoria == 2:
        linhas_executadas = 1, 2, 4, 5, 6, 1, 9
    else:
        if categoria == 3:
            linhas_executadas = 1, 2, 4, 5, 7, 8, 9, 1, 9
        else:
            if categoria == 4:
                linhas_executadas = 1, 2, 4, 5, 7, 8, 10, 11, 12, 19
            else:
                if categoria == 5:
                    linhas_executadas = 1, 2, 4, 7, 8, 10, 11, 13, 14, 15,19
                else:
                    if categoria == 6:
                        linhas_executadas = 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 18, 19
                    else:
                        print('Categoria inválida,digite um numero de 1 a 6')
                        linhas_executadas = 0
print(f'Com a categoria selecionada o números é linhas de {linhas_executadas}')