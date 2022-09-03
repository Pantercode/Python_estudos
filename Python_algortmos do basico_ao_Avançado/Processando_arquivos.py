for x in range(41):
    LARGURA = 79
    with open('entradas1989.txt') as entrada1989:
        for linha in entrada1989.readlines():
            if linha[0] == ';':
                continue
            elif linha[0] == '>':
                print(linha[1:].rjust(LARGURA))
            elif linha[0] == "*":
                print(linha[1:].center(LARGURA))
            else:
                print(linha)