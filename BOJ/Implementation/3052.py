arr = set()

for _ in range(10):
    arr.add(int(input()) % 42)
    
print(len(arr))