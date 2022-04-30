case = [0] * 101

case[1] = 1
case[2] = 1
case[3] = 1

for i in range(98):
    case[i+3] = case[i] + case[i+1]
    
n = int(input())

for _ in range(n):
    k = int(input())
    print(case[k])