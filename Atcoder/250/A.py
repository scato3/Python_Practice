h, w = map(int, input().split())
r, c = map(int, input().split())
ans = 0

for a, b in ((r-1, c), (r+1, c), (r, c+1), (r, c-1)):
    if 1 <= a <= h and 1 <= b <= w:
        ans += 1
print(ans)