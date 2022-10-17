a = int(input())
b = int(input())
c = int(input())

k = list(str(a * b * c))

for i in range(10):
    print(k.count(str(i)))