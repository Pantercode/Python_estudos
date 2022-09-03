distancia = float(input('Qual a distância que deseja viajar: '))
tarifa_menor = 0.50
tarifa_maior = 0.45
if distancia <= 200:
    distancia = distancia +(distancia*tarifa_menor)
    print(f'Sua viagem ficou no valor de R${distancia:6.2f}')
else:
    distancia = distancia+(distancia*tarifa_maior)
    print(f'Sua viagem ficou no valor de R${distancia:6.2f}')

