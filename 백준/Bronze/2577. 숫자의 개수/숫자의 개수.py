tmp = [0] * 10
a = int(input())
b = int(input())
c = int(input())

num = a * b * c
k = str(num)

for i in k:
    tmp[int(i)] += 1

for i in tmp:
    print(i)