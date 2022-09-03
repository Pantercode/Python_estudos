def imprime_lista(L,fimpressao,fcondição):
    for e in L:
        if fcondição(e):
            fimpressao(e)
def imprime_elemento(e):
    print(f'Valor: {e}')
def epar(x):
    return x % 2 == 0
def eimpar(x):
    return not epar(x)


L = [1, 7, 9, 2, 11, 0]
imprime_lista(L,imprime_elemento,epar)
imprime_lista(L,imprime_elemento,eimpar)