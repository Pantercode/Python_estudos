nomes = ['Ana','Carlos','Maria','Marcell', 'Emilly', 'Alana', 'Jose', 'Anthony','James','Tomas']
for tentativas in range(10):
    try:
        i = int(input('Digite o índice que quer imprimir: '))
        print(nomes[i])
    except ValueError:
        print('Digite um numero !')
        raise
    finally:
        print(f'Sempre que o finally é executado*-')