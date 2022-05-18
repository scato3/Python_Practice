from collections import deque

n, k = map(int, input().split())

def move(x):
    data = []
    temp = x
    
    for _ in range(visited[x] + 1):
        data.append(temp)
        temp = moved[temp]
    print(' '.join(map(str, data[::-1])))

def bfs():
    q = deque()
    q.append(n)
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(visited[k])
            move(x)
            return 
        
        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[x] + 1
                moved[i] = x
                q.append(i)
                
                

visited = [0] * 100001
moved = [0] * 100001
bfs()
