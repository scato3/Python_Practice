from itertools import combinations

a, b = map(int, input().split())
arr = list(map(int, input().split())) + [0, 0]
ans = [0] * (b + 1)

for x, y, z in combinations(arr, 3):
    w = x + y + z
    if w <= b:
        ans[w] = 1

print(ans.count(True))