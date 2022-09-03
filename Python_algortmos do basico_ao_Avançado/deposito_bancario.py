meses = 24 * 0.35
x = 1
deposito = 0
while x <= 24:
    valor = float(input(f'Informe {x} depósito: '))
    print(f'Foi depositado {x} e juros do deposito resulta em: {valor*0.014}')
    deposito = deposito + valor
    x = x +1
print(f'A total de de 24 meses você depositou adicionado ao juros {deposito*meses:6.2f}')
