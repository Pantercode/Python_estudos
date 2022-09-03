def fat(n):
    fat = 1
    while fat > 1:
        fat*=n
        n -= 1
    return fat

print(fat(10))
print(fat(3))
