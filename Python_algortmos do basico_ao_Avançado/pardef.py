def epar(n):
    try:
        return n % 2
    finally:
        print('Executado antes de retornar')

try:
    print(2, epar(2))
    print('A', epar('A'))
except Exception:
    print('Algo aconteceu!!')


