def pesquise(lista,valor):
    for a,b in enumerate(lista):
        if a == valor:
            return a
        return None

def soma(L):
    total = 0
    for c in L:
        total+= c
    return total

def media(L):
    total = 0
    for e in L:
        total+=e
    return total / len(L)


L = [10, 20, 25, 30]
print(pesquise(L,25))
print(pesquise(L,2))
print(pesquise(L,5))
print(pesquise(L,15))
print(pesquise(L,10))
