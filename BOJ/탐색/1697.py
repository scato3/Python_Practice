from collections import deque
MAX = 10 ** 5

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        
        if v == K:
            return visited[K]
        for i in (v-1, v-2, v*2):
            if 0 <= i <= MAX and visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)

N, K = map(int, input().split())
visited = [0] * MAX
print(bfs(N))