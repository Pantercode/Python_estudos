listas = ['a',['b','c','d'],'e']
for x in listas:
    if type(x) is str:
        print(x)
    else:
        print(f'Lista', end=' ')
        for z in x:
            print(f'{z}',end=' ')
            print()
