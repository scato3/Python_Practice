n = input().split('-')
arr = []

for i in n:
    s = i.split('+')
    cnt = 0
    for j in s:
        cnt += int(j)
    arr.append(cnt)

num = arr[0]
for i in range(1, len(arr)):
    num -= arr[i]

print(num)