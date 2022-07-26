n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

minVal = cost[0]
sum = 0
for i in range(n-1):
    if minVal > cost[i]:
        minVal = cost[i]
    sum += (minVal * road[i])
print(sum)