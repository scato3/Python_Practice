t = int(input())

for _ in range(t):
    s = list(input())
    c = input()
    arr = []
    ans = 'NO'

    if c not in s:
        print('NO')
    else:
        for i in range(0, len(s), 2):
            if s[i] == c:
                ans = 'YES'
                break
        print(ans)