num1 = int(input('Insira um numero: '))
multiplica = 0
x = 0
while x <= 5:
    multiplica = int(input('Insira outro  numero: '))
    multiplica+=num1
    x+=1
    print(f'{num1} X {multiplica}={num1*multiplica}')
