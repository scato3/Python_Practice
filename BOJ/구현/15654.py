from itertools import permutations

n, m = map(int, input().split())
c = list(map(int, input().split()))
c.sort()

c = permutations(c, m)

for i in c:
    print(' '.join(map(str, i)))