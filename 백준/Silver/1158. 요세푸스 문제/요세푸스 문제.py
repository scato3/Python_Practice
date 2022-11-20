# deque 요세푸스 문제

from collections import deque

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
arr = deque(arr)
res = []

while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    res.append(arr.popleft())

print('<', ', '.join(str(i) for i in res), '>',sep='')