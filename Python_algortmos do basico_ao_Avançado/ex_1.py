def retangulo(largura,altura, carcteres='*'):
    linha = carcteres *largura
    for c in range(altura):
        print(linha)

(retangulo(5,4,"*"))
