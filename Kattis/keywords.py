num = int(input())

seen = {}
count = 0
for i in range(num):
    word = input().replace('-', ' ').lower()
    if word in seen:
        seen[word] = 1
    else:
        seen[word] = 0
        count += 1
print(count)

