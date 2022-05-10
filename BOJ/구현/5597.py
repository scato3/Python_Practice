arr = []
for i in range(1, 31):
    arr.append(i)

for i in range(1, 29):
    arr.remove(int(input()))

print(min(arr))
print(max(arr))