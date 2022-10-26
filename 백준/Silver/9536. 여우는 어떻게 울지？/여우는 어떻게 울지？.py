n = int(input())

for _ in range(n):
    k = dict()
    txt = input().split()
    arr = []
    while True:
        s = input()
        if s == 'what does the fox say?':
            break
        s = s.split()
        k[s[2]] = s[0]
    for i in txt:
        if i not in k:
            arr.append(i)

    for i in arr:
        print(i, end=' ')

