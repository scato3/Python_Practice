n = int(input())
k = 1

while (k * (k+1)) // 2 <= n:
    k += 1

print(k - 1)
