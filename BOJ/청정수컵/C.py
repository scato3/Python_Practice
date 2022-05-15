n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0
max = 0
length = min(len(a), len(b))
for i in range(length):
    if b[i] > a[i]:
        sum += b[i] - a[i]
    if sum > max:
        max = sum
    sum = 0

if len(b) > len(a):
    for i in range(len(b) - len(a)):
        if b[i+len(a)] > max:
            max = b[i+len(a)]

print(max)