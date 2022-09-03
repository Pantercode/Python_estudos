def soma(a,b):
    s = a + b
    return a + b
def subtracao(a,b):
    s = a - b
    return a- b
def imprime(a,b,foper):
    print(foper(a,b))

imprime(5,4, soma)
imprime(5,4, subtracao())