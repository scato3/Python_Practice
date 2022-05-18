n, m = map(int, input().split())

def factorial(k):
    res = 1
    for i in range(k):
        res *= (i+1)
    return res

if m > (n // 2):
    m = n - m

print(factorial(n) // (factorial(m) * factorial(n - m)))

# nCm == n! / m! * (n-m)!