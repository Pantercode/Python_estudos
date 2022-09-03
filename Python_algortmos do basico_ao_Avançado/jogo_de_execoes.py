while True:
    try:
        v = int(input('Digite um numero inteiro (0 para sai): '))
        if v == 0:
            break
    except Exception:
        print('Valor inválido!Redigite')
    else:
        print('Parabéns, nenhuma exceção')
    finally:
        print('Executando sempre,mesmo com o break!')