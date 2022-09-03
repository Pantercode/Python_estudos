a = 'Mundo'
print(f'Alô {a}!!')
preco = 8.90
print(f'Gostaria de R$ {preco:8.2f} de batata.')  #quantidade de espaçamento
print(f'Gostaria de R$ {preco:^8.2f} de batata.') # centralizado
print(f'Gostaria de R$ {preco:<8.2f} de batata.')   # alinhamento a esquerda
print(f'Gostaria de R$ {preco:>8.2f} de batata.') # alinhamento a direita
print(f'Gostaria de R$ {preco:_>8.2f} de batata.') # Anderline
print(f'Gostaria de R$ {preco:.>8.2f} de batata.') # com pontos
x = 5.1
print(f'Inteiro:{int(x)}')
print(f'Preço: R${preco* 10:5.2f}')