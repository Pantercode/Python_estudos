with open("multiplos de 4.txt", "w") as multiplos4:
    with open("pares.txt") as pares:
        for c in pares.readlines():
            if int(c) % 4 == 0:
                multiplos4.write(c)

