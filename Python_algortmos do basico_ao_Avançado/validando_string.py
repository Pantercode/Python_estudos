def valida_texto(string, minimo,maximo):
    while True:
        texto = str(input(string))
        if texto < minimo or texto > maximo:
            print(f'String inválida!, Digite um valor entre {minimo} e {maximo}')
        else:
            return texto