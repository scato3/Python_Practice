a = input()
arr = []
i = 0
while True:
    if a[i:] == a[-1]:
        arr.append(a[i:])
        break
    arr.append(a[i:])
    i += 1

arr.sort()
for i in arr:
    print(i)
