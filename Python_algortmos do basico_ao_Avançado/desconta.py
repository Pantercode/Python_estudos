mercadoria = float(input('Qual o valor do produto: '))
porcentagem = int(input('Qual o desconto: '))
descontos = mercadoria - (mercadoria*porcentagem/100)
print(f'O produto custa  R$ {mercadoria} com desconto %{porcentagem} o produto cai para {descontos}')
