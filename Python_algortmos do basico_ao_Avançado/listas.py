lista_a = ['Nome', 40, 5.55, 10, 'None']
lista_b = lista_a[:]
lista_b[0] = 'Emilly'
print(lista_a, lista_b)
print(lista_a[0:5])
print(lista_b[-1])
print(len(lista_a))
print(len(lista_b))

lista_c =[10, 15, 16, 17, 1000, 49]
x = 0
while x < len(lista_c):
    print(x, end='')
    x+=1