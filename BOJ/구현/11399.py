n = int(input())
time = list(map(int, input().split()))

time.sort()
maxsum = 0
for i in range(n): # 0부터 n까지 for문
    for j in range(i+1): # 0부터 i +1 까지 for문 (즉 1 + 12 + 123 + 1234)
        maxsum += time[j]
        
print(maxsum)