def soma(*args):
    s = 0
    for x in args:
        s += x
        return s


print(soma(2,3))
print(soma(3,15,19,20,21))