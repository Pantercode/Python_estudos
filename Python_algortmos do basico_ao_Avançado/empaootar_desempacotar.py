# def soma(a,b):
#     print(a+b)
#
# Lista = [2,3]
# print(*lista)

def barra(n=10, c='*'):
    print(c * n)
    L =[[5,'-'],[10, '*'], [5], [6,'.']]
    for e in L:
        barra(*e)


print(barra())