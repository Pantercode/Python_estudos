frase = {}
for letra in 'O Rato roeu a roupa do rei de Roma':
    if letra in frase:
        frase[letra] = frase.get(letra) +1
    else:
        frase[letra] = 1
print(frase)