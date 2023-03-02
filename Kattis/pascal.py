import math

def function(n):
    # range(2, int(math.sqrt(n)) + 1) is the range of possible factors of n.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            other_factor = n // i
            return n - other_factor
    return n - 1

n = int(input())
print(function(n))