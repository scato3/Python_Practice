board = [300, 60, 10]

n = int(input())
ans = []
cnt = 0

if n % 10 != 0:
    print(-1)
else:
    for i in board:
        cnt = n // i
        ans.append(cnt)
        n = n % i

for i in ans:
    print(i, end=' ')

