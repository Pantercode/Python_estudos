def imprime_maior(mensagem,*numeros):
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
            print(mensagem,maior)


print(imprime_maior("Maior: ", 5, 4,3,1))
print(imprime_maior("Max: ", *[1,7,9]))