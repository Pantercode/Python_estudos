imposto = 1200
salario = float(input('Informe seu salário: '))
if salario > imposto:
    print(f'Você paga imposto pois recebe R${salario:.2f} e o teto para isenção é R${imposto:.2f}.')
else:
    print(f'Você não imposto pois seu salário é de R${salario:.2f}.')

