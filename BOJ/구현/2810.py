n = int(input())
arr = input()

if arr.count('S') == n :
    print(n)
else:
    arr = arr.replace('LL', 'K')
    print(len(arr) + 1)