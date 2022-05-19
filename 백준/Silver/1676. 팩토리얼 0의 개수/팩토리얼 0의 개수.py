def fac(n):
    k = 1
    for i in range(1, n+1):
        k *= i
    return k

n = int(input())

a = fac(n)
a = str(a)
cnt = 0
for i in range(len(a) - 1, -1, -1):
    if a[i] == '0':
        cnt += 1
    else:
        break

print(cnt)


