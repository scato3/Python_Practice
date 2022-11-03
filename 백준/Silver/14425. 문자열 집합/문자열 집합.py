n, m = map(int, input().split())
arr1 = set()
arr2 = []
cnt = 0

for _ in range(n):
    arr1.add(input())
for _ in range(m):
    arr2.append(input())

for i in arr2:
    if i in arr1:
        cnt += 1
print(cnt)