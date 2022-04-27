from collections import deque

n, k = map(int, input().split())

def bfs(x):
    q = deque()
    q.append(x)
    visited = [0] * 100001
    
    while q:
        x = q.popleft()
        
        if x == k :
            return visited[k]
        
        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001 and visited[i] == 0:
                if i == x*2 and x != 0:
                    visited[i] = visited[x]
                    q.appendleft(i)
                else:
                    visited[i] = visited[x] + 1
                    q.append(i)
    
print(bfs(n))