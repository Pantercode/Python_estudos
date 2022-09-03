import sys

print(f'Numeros de paramêtros:{len(sys.argv)}')
for n,p in enumerate(sys.argv):
    print(f'Parâmetro {n} = {p}')

fparam.py 'primeiro segundo terceiro'
fparam.py '1 2 3'
fparam.py 'readme.txt 5'




