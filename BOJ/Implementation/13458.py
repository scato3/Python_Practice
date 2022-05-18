n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

sum = 0
for i in range(n):
    if a[i] > 0:
        a[i] -= b
        sum += 1
        
    if a[i] > 0:
        sum += a[i] // c
        
        if a[i] % c != 0:
            sum += 1

print(sum)