from itertools import combinations_with_replacement
a, b = map(int, input().split())

c = combinations_with_replacement(range(1, a+1), b)

for i in c:
    print(' '.join(map(str, i)))
    
# combinations랑 다른건 반복되는 요소 있음.