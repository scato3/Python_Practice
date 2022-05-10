from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    
    while q:
        v = q.popleft()
        
        if v == G:
            return count[G]
        
        for i in (v+U, v-D):
            if 0 < i <= F and visited[i] == 0:
                visited[i] = 1
                count[i] = count[v] + 1
                q.append(i)
    
    return 'use the stairs'

visited = [0] * (F+1)
count = [0] * (F+1)
print(bfs(S))
