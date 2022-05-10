n = int(input())

for _ in range(n):
    a, b = input().split()
    arr = []
    for i in range(len(a)):
        if ord(a[i]) > ord(b[i]):
            arr.append(ord(b[i]) + 26 - ord(a[i]))
        else:
            arr.append(ord(b[i]) - ord(a[i]))
    print('Distances:', *arr)