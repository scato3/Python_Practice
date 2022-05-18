arr = list(map(int, input().split()))
a = input()
arr = sorted(arr)

for i in a:
    if i == 'A':
        print(arr[0], end=' ')
    elif i == 'B':
        print(arr[1], end=' ')
    elif i == 'C':
        print(arr[2], end=' ')