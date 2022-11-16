t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = [b[0] - a[0]]

    for i in range(1, n):
        if b[i-1] > a[i]:
            ans.append(b[i] - b[i-1])
        else:
            ans.append(b[i] - a[i])
    print(*ans)