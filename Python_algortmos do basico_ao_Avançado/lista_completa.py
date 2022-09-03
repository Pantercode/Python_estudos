compras = []
while True:
    produto = input('Produto: ')
    if produto == 'fim' or 'Fim' and 'FIM':
        break
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço: '))
    compras.append([produto, quantidade, preco])
    soma = 0.0
    for c in compras:
        print(f'{c[0]:20s} X {c[1]:5d} {c[1]:5.2f} {c[1]} * {c[2]:6.2f}')
        soma += c[1] * c[2]
print(f'O total da compra {soma:7.2f}')