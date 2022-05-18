n = int(input())

def first(x):
    if x == 1:
        return 5000000
    elif 1 < x <= 3:
        return 3000000
    elif 3 < x <= 6:
        return 2000000
    elif 6 < x <= 10:
        return 500000
    elif 10 < x <= 15:
        return 300000
    elif 10 < x <= 21:
        return 100000
    else:
        return 0

def second(x):
    if x == 1:
        return 5120000
    elif 1 < x <= 3:
        return 2560000
    elif 3 < x <= 7:
        return 1280000
    elif 7 < x <= 15:
        return 640000
    elif 15 < x <= 31:
        return 320000
    else:
        return 0

for _ in range(n):
    a, b = map(int, input().split())
    print(first(a) + second(b))