from itertools import combinations_with_replacement

n, m = map(int, input().split())
c = list(map(int, input().split()))
c.sort()

c = combinations_with_replacement(c, m)
c = sorted(list(set(c)))

for i in c:
    print(*i)