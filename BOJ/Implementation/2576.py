arr = []
odd = []

for i in range(7):
    arr.append(int(input()))
    
for i in range(7):
    if arr[i] % 2 == 1:
        odd.append(arr[i])

if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)