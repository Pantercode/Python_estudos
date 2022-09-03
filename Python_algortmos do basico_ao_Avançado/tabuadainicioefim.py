inicio = int(input('Insira o numero para inicio da tabuada: '))
fim = int(input('Insira um número para fim sua tabuada: '))
cont = inicio
while cont <= fim:
    print(f'{cont}X{cont}= {fim*cont}')
    cont+=1