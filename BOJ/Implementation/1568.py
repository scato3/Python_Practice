n = int(input())
k = 1
res = 0

while n > 0:
    if n < k:
        k = 1
    
    n -= k
    k += 1
    res += 1

print(res)
        