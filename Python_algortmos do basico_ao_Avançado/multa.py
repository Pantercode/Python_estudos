velocidade = float(input('Qual velocidade do seu veículo: '))
limite = 80
multa = 5
infracao = (velocidade-limite)*5
if velocidade > limite:
    print(f'Você foi multado em R${infracao:.2f}')
    # if not velocidade > limite:  Para rodar essa condição teria que ser usado  um elif o else
    #     print('Parabéns você está andando de forma segura.')