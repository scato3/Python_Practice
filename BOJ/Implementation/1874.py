n = int(input())
arr1 = []
arr2 = []
cnt = 1
temp = True
for i in range(n):
    k = int(input())
    while cnt <= k:
        arr1.append(cnt)
        arr2.append('+')
        cnt += 1
    if arr1[-1] == k:
        arr1.pop()
        arr2.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in arr2:
        print(i)