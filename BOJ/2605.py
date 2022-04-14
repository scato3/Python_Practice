t = int(input())
num = list(map(int, input().split()))

answer = []

for i in range(t):
    answer.insert(i-num[i], i+1)
    
print(*answer)