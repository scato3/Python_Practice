n = int(input())
arr = list(map(int, input().split()))
k = set(arr)
print(*sorted(k))