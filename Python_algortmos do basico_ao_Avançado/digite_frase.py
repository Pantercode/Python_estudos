def digite_frase():
    frase = 'Paradigma'.lower()
    resp = 'n'
    while True:
        texto = input('Digite uma letra: ').lower()[0]
        if texto in frase:
            print(f'A vogal {texto} está contida na frase secreta.')
        else:
            print(f'A vogal {texto} digitada não está contida')
        resp = input('Deseja fazer outra tentativa [S/N]: ').upper()[0]
        if resp == 's':
         print(texto)
        else:
            print('Saindo')
            break



print(digite_frase())