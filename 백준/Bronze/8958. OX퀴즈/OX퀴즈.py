n = int(input())

for _ in range(n):
    k = input()
    cnt = 0
    ans = 0
    for i in range(len(k)):
        if k[i] == 'O':
            cnt += 1
            ans += cnt
        if k[i] == 'X':
            cnt = 0
    print(ans)

