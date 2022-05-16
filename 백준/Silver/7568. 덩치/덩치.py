n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
    
for i in arr:
    rank = 1
    for j in arr:
        if j[0] > i[0] and j[1] > i[1]:
            rank += 1

    print(rank, end= ' ')