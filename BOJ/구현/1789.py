n = int(input())
i = 0
while True:
    i += 1
    if (i * (i+1)) // 2 > n:
        break
    
print(i - 1)