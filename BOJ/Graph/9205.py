from collections import deque

T = int(input())

def bfs():
    q = deque()
    q.append(start)
    visited = [0] * n
    
    while q:
        x, y = q.popleft()
        
        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            return 1
        for i in range(n):
            nx, ny = graph[i]
            if visited[i] == 0:
                if abs(x- nx) + abs(y - ny) <= 1000:
                    visited[i] = 1
                    q.append((nx, ny))
    return 0

for _ in range(T):
    n = int(input())
    start = list(map(int, input().split()))
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    end = list(map(int, input().split()))
    
    res = bfs()
    if res:
        print('happy')
    else:
        print('sad')
    