n, k = map(int, input().split())
lst = list()
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)
count = 0

for i in range(n):
    count += k // lst[i]
    k = k % lst[i]

print(count)