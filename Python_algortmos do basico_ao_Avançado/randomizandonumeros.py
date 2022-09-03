from aleatorios import randint

segredo = randint(1, 10)
print("Bem Vindo!")
cont = 0
while cont != segredo:
    resposta = input("Escolha um número: ")
    cont = int(resposta)
    if cont == segredo:
        print("Acertou!!, Você ganhou")
    else:
        if cont > segredo:
            print("Você digitou um número muito alto!")
            print("Digite novamente")
        else:
            print("Você digitou um número muito baixo!")
            print("Digite novamente")
print('Fim')