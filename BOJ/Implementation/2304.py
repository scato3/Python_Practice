n = int(input())

arr = []
maxH = 1
maxL = 0
for _ in range(n):
    L, H = map(int, input().split())
    arr.append((L, H))
    if L > maxL : 
        maxL = L
    if H > maxH:
        maxH = H
        maxIndex = L
        
check = [0] * (maxL + 1)

for l, h in arr:
    check[l] = h

temp = 0
ans = 0
for i in range(maxIndex + 1): #앞에서 부터 maxIndex까지
    if check[i] > temp:
        temp = check[i]
    ans += temp

temp = 0

for i in range(maxL, maxIndex, -1): # 뒤에서부터 maxIndex 바로 뒤까지
    if check[i] > temp:
        temp = check[i]
    ans += temp

print(ans)