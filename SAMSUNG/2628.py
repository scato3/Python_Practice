m, n = map(int, input().split())
sero = [0, m]
garo = [0, n]
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    if a == 1:
        sero.append(b)
    else:
        garo.append(b)

sero.sort()
garo.sort()
ans = 0
for i in range(len(sero) - 1):
    for j in range(len(garo) - 1):
        ans = max(ans, (sero[i+1] - sero[i]) * (garo[j+1] - garo[j]))

print(ans)
