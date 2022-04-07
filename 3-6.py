n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k # 나머지를 제외한 k의 배수 중 가장 큰 값
    result += (n - target) # result에 몇 번 1을 뺄건지에 대한 값
    n = target # 다시 n에 target을 넣는다!
    
    if(n < k):
        break
    result += 1
    n = n // k
    
result += (n - 1)
print(result)