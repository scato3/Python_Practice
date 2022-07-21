a, b = map(int, input().split())
arr1 = set()
arr2 = set()
ans = []
for i in range(a):
    arr1.add(input())
for i in range(b):
    arr2.add(input())
for i in arr1:
    if i in arr2:
        ans.append(i)
print(len(ans))
ans.sort()
for i in ans:
    print(i)
