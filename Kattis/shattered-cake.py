import math
a = int(input())
b = int(input())

i = 0
total = 0
while i < b:
    c = map(int, input().split())
    d = math.prod(c)
    total += d
    i += 1
print(total // a)