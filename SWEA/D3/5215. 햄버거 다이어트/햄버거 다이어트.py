t = int(input())

for tc in range(1, t+1):
    n, l = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    result = [[] for _ in range(n)]

    for i in range(n):
        result[i].append(data[i])
        for j in range(i):
            for score, cal in result[j]:
                if cal + data[i][1] <= l:
                    result[i].append((score + data[i][0], cal + data[i][1]))

    max_score = 0

    for i in range(n):
        for score, cal in result[i]:
            if score > max_score:
                max_score = score

    print('#{} {}'.format(tc, max_score))

