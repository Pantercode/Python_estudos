frase = {}
for letra in 'Abracadabra':
    if letra in frase:
        frase[letra] = frase[letra] +1
    else:
        frase[letra] = 1
print(frase)