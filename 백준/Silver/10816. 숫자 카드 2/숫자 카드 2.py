from collections import Counter

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

cnt_card = Counter(arr1)
ans = []

for i in arr2:
    if i in cnt_card:
        ans.append(cnt_card[i])
    else:
        ans.append(0)

for i in ans:
    print(i,end=' ')