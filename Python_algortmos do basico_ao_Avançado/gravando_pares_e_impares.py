with open('ímpares.txt',"w")as ímpares:
    with open('pares.txt',"w")as pares:
        for c in range(0,1000):
            if c % 2 == 0:
                pares.write(f'{c}\n')
            else:
                ímpares.write(f'{c}\n')