frase_1 = 'AABBEFAAT'
frase_2 = 'BE'
p = 0
while(p <= 1):
    p = frase_1.find('BE', p)
    if frase_2 not in frase_1:
        continue
    print(f'Posição: {p}')
    p += 1
    print(frase_1 + frase_2)