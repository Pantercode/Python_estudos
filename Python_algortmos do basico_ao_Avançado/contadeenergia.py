kwh = int(input('Qual o consumo de kwh foi gasto em sua residência: '))
padrao = str(input('Qual o seu tipo de instalação:[R = Residencial/I = Indústria/C = Comercial] ')).strip().upper()[0]

if padrao == 'R' and kwh > 500:
    energia = kwh * 0.65
elif padrao == 'R' and kwh <= 500:
    energia = kwh * 0.40
elif padrao == 'I' and kwh > 500:
    energia = kwh * 0.60
elif padrao == 'I' and kwh <= 500:
    energia = kwh * 0.55
elif padrao == 'C' and kwh > 500:
    energia = kwh * 0.60
else:
   energia = kwh * 0.55
print(f'A fatura de consumo gerou um valor {energia:6.2f} ')