arr = set()
for i in range(1, 10001):
    i = i + sum(map(int, str(i)))
    arr.add(i)

for i in range(1, 10001):
    if i not in arr:
        print(i)