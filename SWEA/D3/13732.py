T = int(input())
 
for t in range(T):
    N = int(input())
    lst = [input() for _ in range(N)]
    dots = []
    result = 'yes'
 
    for i in range(N):
        for j in range(N):
            if lst[i][j] == '#':
                dots.append((i, j))
                
    if len(dots) == 1:
        result = 'yes'
    elif len(dots) ** 0.5 != int(len(dots) ** 0.5):
        result = 'no'