n, k = map(int, input().split())
country = []
for _ in range(n):
    country.append(list(map(int, input().split())))
    
country.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for i in range(n):
    if country[i][0] == k:
        idx = i
        
for i in range(n):
    if country[idx][1:] == country[i][1:]:
        print(i+1)
        break