n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0]

tmp = 0
for i in arr:
    tmp += i
    prefix.append(tmp)

for i in range(m):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a-1])