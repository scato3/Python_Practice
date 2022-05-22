t = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

sum = 0
for i in range(t):
    sum += max(arr2) * min(arr1)
    arr1.remove(min(arr1))
    arr2.remove(max(arr2))
print(sum)