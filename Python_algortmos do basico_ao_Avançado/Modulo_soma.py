from entrada import valida_inteiro

L = []
for x in range(10):
    L.append(valida_inteiro('Digite um numero:', 0, 20))
print(f'Soma: {sum(L)}')