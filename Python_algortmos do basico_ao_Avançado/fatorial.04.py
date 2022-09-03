def fatorial(n):
    print(f'Calculando o fatorial de {n}')
    if n == 1 or n == 0:
        print(f'O fatorial de {n} = 1')
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f'fatorial de {n} = {fat}')
        return fat

fatorial(4)
fatorial(100)
fatorial(500)
