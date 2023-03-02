num = int(input())

for x in range(num):
    i, value = input().split()
    length = len(value)

    octal = 0
    hex = 0
    for x in range(length):
        octal += int(value[x]) * 8 **(length - x - 1)
        hex += int(value[x]) * 16 **(length - x - 1)
    
    if max(map(int, list(value))) > 7: # if the max value is greater than 7, it's not octal
        octal = 0

    print(i, octal, int(value), hex)