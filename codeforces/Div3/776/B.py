t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    arr = []
    for i in range(1, b+1):
        arr.append((i // c) + (i % c))

    print(arr)
