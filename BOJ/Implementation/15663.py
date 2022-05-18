from itertools import permutations

n, m = map(int, input().split())

c = list(map(int, input().split()))

c = permutations(c, m)
c = sorted(list(set(c)))

for i in c:
    print(' '.join(map(str, i)))