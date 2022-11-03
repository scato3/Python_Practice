n = list(input())
n.sort(reverse=True)
tmp = 0

for i in n:
    tmp += int(i)

if tmp % 3 != 0 or '0' not in n:
    print(-1)
else:
    for i in n:
        print(i, end='')