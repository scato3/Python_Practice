t = int(input())
arr = set()
max = 0
ans = 0
for i in range(1, t+1):
    a, b = input().split()
    b = int(b)
    if a in arr:
        continue
    arr.add(a)
    if b > max:
        max = b
        ans = i

print(ans)

