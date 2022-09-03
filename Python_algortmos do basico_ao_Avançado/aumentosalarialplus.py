salario = float(input('Informe seu salário para calculo de reajuste: '))
base = salario
aumento = 0
if base >= 1250:
    aumento = aumento +((base +1250) * 0.10)
    print(f'Salario: R${salario:6.2f} Aumento: R${aumento: 6.2f}')
    base = 1250
if base < 1250:
    aumento = aumento +((base +1250) * 0.15)
    print(f'Salario: R${salario:6.2f} Aumento: R${aumento: 6.2f}')
