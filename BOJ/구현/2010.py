n = int(input())
maxsum = 0

for _ in range(n):
    maxsum += int(input())
    
print(maxsum - (n - 1))