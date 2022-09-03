lista = [0] * 10
hash('A')
print(hash('A'))
lista[hash('A') % 10] = 'A'

print(lista)