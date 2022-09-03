dias = 60
km = 0.15
tempo_alugado = int(input('Quantos dias  você ficou com veículo: '))
km_rodado = int(input('Quantos Km você rodou: '))
diaria = tempo_alugado * dias
quilometragem = km * km_rodado
total = quilometragem + diaria

print('====================================')
print('        Recibo Detalhado           ')
print('====================================')
print(f'       Total dias R${diaria:.2f}  ')
print('=====================================')
print(f'    Total km R${quilometragem:.2f}')
print('=====================================')
print(f'      Total do reciboR${total:.2f}')
print('====================================')
