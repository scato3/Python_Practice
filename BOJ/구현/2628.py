n, m = map(int, input().split())
garo = [0, n]
sero = [0, m]

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    
    if a == 1:
        garo.append(b)
    else:
        sero.append(b)
        
garo.sort(reverse=True)
sero.sort(reverse=True)
max = 0
for i in range(len(sero) - 1):
    for j in range(len(garo) - 1):
        if (garo[j] - garo[j+1]) * (sero[i] - sero[i+1]) > max:
            max = (garo[j] - garo[j+1]) * (sero[i] - sero[i+1])

print(max)