listas = [1,[2,3,4,[5, 6, 7]]]
for x in listas:
    if type(x) is int:
        print(x)
    else:
        print(f'Lista', end=' ')
        for z in x:
            print(f'{z}',end=' ')
            print()
