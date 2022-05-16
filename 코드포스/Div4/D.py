N = int(input())

for _ in range(N):
    n = int(input())
    a = list(input())
    arr = set()
    for i in range(n):
        if a[i] == 'W':
            if len(arr) == 1:
                print('NO')
                break
            else:
                arr = set()
        else:
            arr.add(a[i])
    else:
        if len(arr) != 1:
            print('YES')
        else:
            print('NO')