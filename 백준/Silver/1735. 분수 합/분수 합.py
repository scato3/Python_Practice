import math

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

k = a1 * b2 + a2 * b1
tmp = a2 * b2

aa = math.gcd(k, tmp)
k //= aa
tmp //= aa
print(k, tmp)