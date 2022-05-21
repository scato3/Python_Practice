from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    cnt = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                    if graph[nx][ny] == 1:
                        visited[nx][ny] = 1
                        graph[nx][ny] = 0
                        cnt += 1
    res.append(cnt)
    return cnt
res = []
time = 0
while True:
    visited = [[0] * m for _ in range(n)]
    time += 1
    ans = bfs()
    if ans == 0:
        break

print(time - 1)
print(res[-2])


