def soma(a,b,imprime=False):
    s = a + b
    if imprime:
        print(s)
    return s

def soma2(imprime=True, a, b):
    s1 = a + b
    if imprime:
        print(s1)
    return s


print(soma(4,6))
print(soma(4,6,True))
print(soma2(6,7))