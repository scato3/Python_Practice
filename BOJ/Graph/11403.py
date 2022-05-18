from collections import deque

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
visited = [[0] * n for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append(x)
    visit = set()
    while q:
        x = q.popleft()
        visit.add(x)
        next_row = graph[x]
        for i in range(len(next_row)):
            if next_row[i] == 1:
                if i == y:
                    return 1
                elif i not in visit:
                    q.append(i)
                    visit.add(i)
    return 0

for x in range(n):
    for y in range(n):
        visited[x][y] = bfs(x, y)
    print(*visited[x])

