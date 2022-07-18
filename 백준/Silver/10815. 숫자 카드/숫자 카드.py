n = int(input())
arr1 = set(map(int, input().split()))
num = int(input())
arr2 = list(map(int, input().split()))
ans = []
for i in arr2:
    if i in arr1:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)