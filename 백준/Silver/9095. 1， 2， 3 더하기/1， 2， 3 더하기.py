n = int(input())
def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-3) + sol(n-2) + sol(n-1)

for i in range(n):
    k = int(input())
    print(sol(k))