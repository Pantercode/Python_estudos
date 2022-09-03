cont = 0
while True:
    num = int(input('Digite um numero inteiro ou 0 para sair: '))
    if num == 0:
        break
    cont += num
print(f'Você digitou os numeros {num*num/num}')
