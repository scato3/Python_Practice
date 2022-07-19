n = int(input())
for _ in range(n):
    a = input()
    s = list(a)
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        if cnt < 0:
            print('NO')
            break
    if cnt > 0:
        print('NO')
    if cnt == 0:
        print('YES')