numeros = [9, 8, 7, 12, 0, 13, 21]
pares = []
impares = []
for c in numeros:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f'Os números pares são {pares}')
print(f'Os número ímpares saõ {impares}')