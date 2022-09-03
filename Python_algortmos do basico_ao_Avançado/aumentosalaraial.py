s = float(input('Informe o salário: '))
p = int(input('Informe a porcentagem do aumento: '))
a = s+(s * p/100)

print(f"O salário de R$ {s:.2f} com o reajuste de %{p} foi elevado para R$ {a:.2f}.")