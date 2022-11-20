# 딕셔너리 기본

dic = {}

for _ in range(int(input())):
    a, b = input().split()

    if b == 'enter':
        dic[a] = 1
    else:
        del dic[a]
k = sorted(dic, reverse=True)
for i in k:
    print(i)
