from collections import deque

a, b = map(int, input().split())
q = deque()
for i in range(1, a+1):
    q.append(i)
print('<',end='')
while q:
    for _ in range(b-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(),end='')
    if q:
        print(', ',end='')
print('>')
