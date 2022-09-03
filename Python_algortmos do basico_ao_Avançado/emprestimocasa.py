
salario = float(input('Informe seu salário: '))
casa = float(input('Qual o valor da casa que você escolheu: '))
anos = int(input('Quantos anos você quer financiar a casa: '))
meses = anos * 12
prestacao = casa / meses
if prestacao > salario*0.3:
    print('O empréstimo não pode ser concedido')
else:
    print(f'O empréstimo  pode ser concedido e será no valor de R${prestacao:6.2f} ')