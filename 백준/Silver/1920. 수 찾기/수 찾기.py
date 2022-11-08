N = int(input())
A = set(map(int, input().split()))
M = int(input())
K = list(map(int, input().split()))

for i in K:
    print(1) if i in A else print(0)