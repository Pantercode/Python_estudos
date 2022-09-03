EMPRESA = 'Unidos venceremos Ltda'
def imprime_cabeçalho():
    print('EMPRESA')
    print("-" * len(EMPRESA))



a = 5
def muda_e_imprime():
    global a
    a = 7
    print(f'A dentro da função: {a}')
    print(f'a antes de mudar : {a}')
    muda_e_imprime()
    print(f'a depois de mudar: {a}')


print(imprime_cabeçalho())
print(muda_e_imprime())