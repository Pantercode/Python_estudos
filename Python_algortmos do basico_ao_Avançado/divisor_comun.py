def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


print(mdc(10, 6))
print(mdc(8, 4))
