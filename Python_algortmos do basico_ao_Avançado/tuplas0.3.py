*a, b = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(b)
*b, a = [1, 2, 3, 4, 5, 6, 7]
print(b)
print(a)
a, *b, c = *b, a = [1, 2, 3, 4, 5, 6, 7]
print(a)
print(b)
print(c)
a, b, *c = *b, a = [1, 2, 3, 4, 5, 6, 7]
print(c)
print(b)
print(a)
