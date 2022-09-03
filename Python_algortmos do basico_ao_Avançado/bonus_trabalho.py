from time import sleep


print('\033[31m================================================================\033[m')
tempo_trabalhado = int(input('Quantos anos você trabalha conosco: '))
valor_do_bonus = float(input('Qual a porcentagem do bônus: '))
aumento = valor_do_bonus * tempo_trabalhado
print('\033[31m==================================================================\033[m')
print('calculando aguarde!')
print('...')
sleep(3)
sleep(2)
print('.........................')
print('carregando')
sleep(1)
print(f'Seu aumento é de {aumento}!')
