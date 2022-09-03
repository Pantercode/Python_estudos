L = [1, 2, 3, 4, 5, 6]
I = iter(L)
print(I)

print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
#print(next(I))  Caso não tenha mais elementos na lista retorna uma exeçeção StopIteration.


L = {1, 2, 3, 4, 5, 6}
I = iter(L)
print(I)
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))