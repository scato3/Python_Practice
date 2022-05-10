n = int(input())
arr = list(map(int, input().split()))
ans = set(arr)

print(len(arr) - len(ans))