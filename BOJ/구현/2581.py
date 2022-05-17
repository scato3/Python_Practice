n = int(input())
m = int(input())

ans = []
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1
        
for i in range(n, m+1):
    if i <= 1:
        continue
    else:
        if isPrime(i) == 1:
            ans.append(i)
if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)