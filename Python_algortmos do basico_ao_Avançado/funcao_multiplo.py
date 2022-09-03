def multiplos(x,y):
    if x % 3 == 0:
       return print(f'O numero {x} é um número primo.')
    else:
        print(f'O numero {x} não é um número primo.')
        if y % 3 == 0:
            print(f'O numero {y} é primo')
        else:
            print(f'O numero {y} não é um número primo.')



multiplos(3,10)
multiplos(2,2)