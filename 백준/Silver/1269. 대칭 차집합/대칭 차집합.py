a, b = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = set(arr1)
arr2 = set(arr2)

print(len(arr2 - arr1) + len(arr1 - arr2))