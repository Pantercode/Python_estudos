L= [15, 7, 27, 39]
num1 = int(input('Digite o valor a procurar: '))
num2 = int(input('Digite outro valor a procurar: '))
achou = False
x = 0
while x < len(L):
    if L[x] == num1:
        achou = True
    elif L[x] == num2:
        achou = True
        break
    x+=1
if achou:
    print(f'{num1} foi encontrado  {L} ')
    print(f'e {num2} foi encontrado  {L}')
else:
    print(f'{num1} e {num2} não foi encontrado')