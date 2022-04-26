from itertools import combinations

a, b = map(int, input().split())
c = combinations(range(1, a+1), b)

for i in c:
    print(' '.join(map(str, i)))