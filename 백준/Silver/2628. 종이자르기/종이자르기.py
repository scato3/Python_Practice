n, m = map(int, input().split())

t = int(input())

sero = [0, m]
garo = [0, n]

for _ in range(t):
    a, b = map(int, input().split())
    
    if a == 1:
        garo.append(b)
    else:
        sero.append(b)

garo.sort()
sero.sort()
answer = 0

for i in range(len(sero) - 1):
    for j in range(len(garo) - 1):
        answer = max(answer, (garo[j+1]-garo[j]) * (sero[i+1] - sero[i]))
        
print(answer)
              
        
        