n = int(input())
arr = list(map(int, input().split()))

tmp = [arr[0]]

for i in range(n - 1):
    tmp.append(max(tmp[i] + arr[i+1], arr[i+1]))

print(max(tmp))