A, B, C = map(int, input().split())
visited = [0] * 101

for _ in range(3):
    a, b = map(int, input().split())
    
    for i in range(a, b):
        visited[i] += 1
        
sum = 0
for i in visited:
    if i == 1:
        sum += i * A
    if i == 2:
        sum += i * B
    if i == 3:
        sum += i * C

print(sum)