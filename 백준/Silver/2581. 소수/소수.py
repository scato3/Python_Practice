m = int(input())
n = int(input())

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1

ans = []
for i in range(m, n+1):
    if i <= 1:
        continue
    if isPrime(i) == 1:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))