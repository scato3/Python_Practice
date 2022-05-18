n = int(input())

for _ in range(n):
    pts = list(map(int, input().split()))
    pts.sort()
    del pts[0]
    del pts[-1]
    if max(pts) - min(pts) >= 4:
        print('KIN')
    else:
        print(sum(pts))