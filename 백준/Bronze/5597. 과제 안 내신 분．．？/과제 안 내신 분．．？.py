arr = []

for i in range(1, 31):
    arr.append(i)
    
for i in range(1, 29):
    arr.remove(int(input()))
    
print(arr[0])
print(arr[1])