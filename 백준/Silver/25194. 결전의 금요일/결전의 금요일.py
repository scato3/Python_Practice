n = int(input())
lst = list(map(int, input().split()))
lst.sort()
arr = [0]
sum = 0

for i in lst:
    arr.append(arr[-1] + i)
flag = 0
for i in range(1, len(arr)):
    if flag:
        break
    for j in range(i):
        now = arr[i] - arr[j]
        
        if now % 7 == 4:
            flag = 1
            break

if flag:
    print('YES')
else:
    print('NO')