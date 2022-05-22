n = int(input())
arr1 = list(map(int, input().split()))
t = int(input())
arr2 = list(map(int, input().split()))

cnt = {}
for i in arr1:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in arr2:
    res = cnt.get(i)
    if res == None:
        print(0, end=' ')
    else:
        print(res, end=' ')