n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = []
for i in range(len(a)):
    if a[i] == max(a):
        arr.append(i + 1)

flag = 0
for i in b:
    if i in arr:
        flag = 1
        break

if flag:
    print('Yes')
else:
    print('No')