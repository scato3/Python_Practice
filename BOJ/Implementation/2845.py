a, b = map(int, input().split())
sum = a * b

num = list(map(int, input().split()))

for i in num:
    print(i - sum, end=' ')