num = int(input())

seen = {}
for i in range(num):
    n = int(input())

    count = 0
    for i in range(n):
        city = input()
        if city in seen: # if city is in seen
            seen[city] = 1 # set the value to 1
        else:    # if city is not in seen
            seen[city] = 0 # set the value to 0
            count += 1 # and increment count
    print(count)