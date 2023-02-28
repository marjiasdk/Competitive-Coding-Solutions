import math

line = input()
x1, y1, x2, y2 = line.split(" ")

result = math.sqrt(((float(x2) - float(x1)) ** 2) * ((float(y2) - float(y1)) ** 2))
print(round(result, 3))