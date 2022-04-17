arr = []
odd = []

for _ in range(7):
    arr.append(int(input()))
    
for i in range(7):
    if arr[i] % 2 != 0:
        odd.append(arr[i])

if len(odd) == 0:
    print(-1)

else:
    print(sum(odd))
    print(min(odd))