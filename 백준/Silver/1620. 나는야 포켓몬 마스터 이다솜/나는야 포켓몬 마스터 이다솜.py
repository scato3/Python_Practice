n, m = map(int, input().split())
dic = {}
arr = []

for i in range(1, n+1):
    a = input()
    dic[i] = a
    dic[a] = i

for i in range(m):
    k = input()
    if k.isdigit():
        print(dic[int(k)])
    else:
        print(dic[k])
