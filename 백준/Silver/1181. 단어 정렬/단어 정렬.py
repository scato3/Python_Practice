n = int(input())
arr = []
for i in range(n):
    a = input()
    arr.append(a)

lst = set(arr)
tmp = list(lst)
tmp.sort()
tmp.sort(key = len)

for i in tmp:
    print(i)