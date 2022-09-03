nomes = ['Ana','Carlos','Maria','Marcell', 'Emilly', 'Alana', 'Jose', 'Anthony','James','Tomas']
for tentativas in range(10):
    try:
        i = int(input('Digite o índice que quer imprimir: '))
        print(nomes[i])
    except ValueError:
        print('Digite um numero !')
    except IndexError:
        print('Valor inválido, digite entre 0 a 2')
    finally:
        print(f'Tentivas {tentativas +1}')