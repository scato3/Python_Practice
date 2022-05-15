n = list(input())
a = n
sum = 0
cnt = 0

if len(n) == 1:
    for i in n:
        sum += int(i)
else:
    while True:
        cnt += 1
        for i in a:
            sum += int(i)
        if len(str(sum)) == 1:
            break
        a = str(sum)
        sum = 0

print(cnt)
if sum % 3 == 0:
    print('YES')
else:
    print('NO')