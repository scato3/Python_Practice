t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if b % a != 0:
        print(0, 0)
    else:
        print(1, b // a)