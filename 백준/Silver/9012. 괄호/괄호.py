n = int(input())

for _ in range(n):
    a = input()
    s = list(a)
    tmp = 0
    for i in s:
        if i == '(':
            tmp += 1
        if i == ')':
            tmp -= 1
        if tmp < 0:
            print('NO')
            break
    if tmp > 0:
        print('NO')
    if tmp == 0:
        print('YES')