produto1 = ['maças', 10, 0.30]
produto2 = ['perâ', 5, 0.75]
produto3 = ['kiwi', 4, 0.98]
compras = [produto1, produto2, produto3]
for c in compras:
    print(f'Produto: {c[0]}')
    print(f'Quantidade: {c[1]}')
    print(f'Preço: {c[2]:5.2f}')