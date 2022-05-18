n = int(input())
A = 100
B = 100

for _ in range(n):
    a, b = map(int, input().split())
    
    if a > b:
        B = B - a
    if a < b:
        A = A - b
    if a == b:
        continue

print(A)
print(B)