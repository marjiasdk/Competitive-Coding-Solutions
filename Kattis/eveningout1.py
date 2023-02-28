a, b = map(int, input().split())

if a % b == 0:
    print(0)
else:
    diff = b - (a % b)
    if diff <= a % b:
        print(diff)
    else:
        print(b - diff)
