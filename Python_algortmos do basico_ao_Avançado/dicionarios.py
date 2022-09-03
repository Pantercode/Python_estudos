tabela = {
    'Alface': 0.45,
    'Batata': 1.20,
    'Tomate': 2.30,
    'Feijão': 1.50}
print(tabela['Tomate'])
tabela['Tomate'] = 9.95
tabela['Cebola'] = 3.95
print(tabela['Cebola'])
print(tabela)
print('Manga' in tabela)  #verificando
print(tabela.keys())
print(tabela.values())