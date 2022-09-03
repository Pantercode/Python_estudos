Lista = [x for x in range(10)]
print(Lista)

lista1 = [x for x in range(100)]
print(lista1)

lista2 = [x * 2 for x in [0,5,6,7,4,['Marcell','Oliveira']]]
print(lista2)

lista3 = [(x,x *2) for x in [1, 2, 3]]
print(lista3)

lista4 =[s.upper() for s in 'zxcvbnmasdfghjklçqwertyuiop']
print(lista4)

lista5 = [x for x in range(10) if x % 2 == 0]
print(lista5)

lista6 = [x for x in range(0, 10, 2)]
print(lista6)

lista7 = list(range(0,10,2))
print(lista7)

lista8 = [(x, y) for x,y in[(4,3), (1,2), (8,9)]]
print(lista8)

lista9 = [(x, y) for * x,y in[(4,3), (1,2), (8,9)]]
print(lista8)

lista10 = [(x, y) for x,*y in[(4,3), (1,2), (8,9)]]
print(lista10)