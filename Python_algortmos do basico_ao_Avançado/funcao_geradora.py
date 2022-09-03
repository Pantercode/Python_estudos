def gerador_de_numeros():
    i = 0
    while True:
        yield
        i += 1

g = gerador_de_numeros()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for x in gerador_de_numeros():
    print(x)