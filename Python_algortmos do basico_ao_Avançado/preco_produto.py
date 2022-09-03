tabela = {'Couve': 1.50,
          'Batata': 1.20,
          'Tomate': 9.98,
          'Feijão':1.50}
while True:
    produto = input('Digite o nome do produto,"Fim" para terminar: ').capitalize()
    if produto == 'Fim':
        break
    if produto in tabela:
        print(f'Preço{tabela[produto]:5.2f}')
    else:
        print('O produto não foi encontrado')
print(f'Os produtos contidos na tabela são {tabela}')
