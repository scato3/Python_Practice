from collections import deque
MAX = 10 ** 5

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v == K:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= MAX and not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)

N, K = map(int, input().split())
visited = [0 for _ in range(MAX+1)]
print(bfs(N))

