def faixa_int(pergunta,minimo=0,maximo=10):
    while True:
        v = int(input(pergunta))
        if v < minimo or V > maximo:
            print(f'Valor inválido.Digite um numero entre {minimo} e {maximo}')
        else:
            return v




print(faixa_int(1,2,5))
