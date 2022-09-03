compras = []
while True:
    produtos = input('Digite o produto a ser adicionado na lista de compras(digite "Fim" para sair): ').upper()
    if produtos == 'FIM':
        break
    else:
        compras.append(produtos)
for p in compras:
    print(p)

print(compras)
