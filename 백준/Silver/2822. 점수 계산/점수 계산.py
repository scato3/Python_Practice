arr = []

for _ in range(8):
    arr.append(int(input()))
k = sorted(arr, reverse=True)
temp = []

for i in range(5):
    temp.append(k[i])

print(sum(temp))
temp1 = []
for i in temp:
    temp1.append(arr.index(i) + 1)

temp1.sort()
print(*temp1)