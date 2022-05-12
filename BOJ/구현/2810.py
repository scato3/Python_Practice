n = int(input())
lst = input()

if lst.count('S') == n:
    print(n)
else:
    lst = lst.replace('LL', 'K')
    print(len(lst) + 1)