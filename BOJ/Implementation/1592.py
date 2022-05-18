n, m, l = map(int, input().split())
visited = [0] * (n+1)

i = 0
cnt = 0
while True:
    visited[i] += 1
    
    if visited[i] == m:
        print(cnt)
        break
    
    if visited[i] % 2 == 1:
        i = (i + l) % n
    else:
        i = (i - l) % n
    
    cnt += 1

