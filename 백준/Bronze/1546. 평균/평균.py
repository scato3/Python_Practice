n = int(input())
arr = list(map(int, input().split()))
tmp = 0
first = max(arr)
for i in arr:
    tmp += i / first * 100

print(tmp / n)
