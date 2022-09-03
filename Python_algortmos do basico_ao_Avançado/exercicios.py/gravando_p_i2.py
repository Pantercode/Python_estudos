with open('ímpares2.txt',"w")as ímpares,open('pares2.txt',"w")as pares
    for c in range(0,1000):
        if c % 2 == 0:
            pares.write(f'{c}\n')
        else:
            ímpares.write(f'{c}\n')