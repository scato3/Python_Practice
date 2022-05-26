n, k = map(int, input().split())
female = [0] * 1000
male = [0] * 1000

for i in range(n):
    a, b = map(int, input().split())

    if a == 0:
        female[b] += 1
    else:
        male[b] += 1
cnt = 0
for i in range(1, 7):
    if female[i] % k == 0:
        cnt += female[i] // k
    else:
        cnt += (female[i] // k) + 1
    if male[i] % k == 0:
        cnt += male[i] // k
    else:
        cnt += (male[i] // k) + 1


print(cnt)
