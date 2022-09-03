def pesquisa(lista,valor):
    for c, d in enumerate(lista):
        if c == valor:
            return c
        return None


L = [10,20,25,30]
print(pesquisa(L,25))
print(pesquisa(L,27))
print(pesquisa(L,10))