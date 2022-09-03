import sys


if len(sys.argv) != 2:
    print("\nFparam.py primeiro segundo terceiro\n\n")
    print("\nFparam.py 1 2 3\n\n")
    print("\nFparam.py readme.txt\n\n")
else:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
    for linha in arquivo.readlines():

        print(linha[:-1])
    arquivo.close()