n, m = map(int, input().split())

dic = {}

for i in range(1, n+1):
    a = input()
    dic[i] = a
    dic[a] = i

for i in range(m):
    b = input()
    if b.isdigit():
        print(dic[int(b)])
    else:
        print(dic[b])