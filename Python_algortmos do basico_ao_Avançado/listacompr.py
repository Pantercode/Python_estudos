import math

c = [math.sqrt(z) for z in range(0, 10)]
print(c)

d = [z for z in range(0,10) if math.sqrt(z) % 1 == 0]
print(d)