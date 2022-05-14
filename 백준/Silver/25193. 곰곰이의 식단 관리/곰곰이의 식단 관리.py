from math import ceil

n = int(input())
arr = list(input())

c = 0
for i in range(n):
    if arr[i] == 'C':
        c += 1
d = n - c

print(ceil(c / (d+1)))
