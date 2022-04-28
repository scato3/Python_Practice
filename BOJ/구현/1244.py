N = int(input())
arr = [-1] + list(map(int, input().split())) # 0 값을 -1을 넣어줘어 인덱스 접근을 용이하게 만든다.
n = int(input())

def change(x):
    if arr[x] == 0:
        arr[x] = 1
    else:
        arr[x] = 0
    return

for _ in range(n):
    sex, num = map(int, input().split())
    
    if sex == 1:
        for i in range(num, N+1, num): # num 값으로 시작하면서 num의 배수를 change 해준다.
            change(i)
    else:
        change(num) # 일단 num에 해당하는 값 바꿔준다.
        
        for k in range(N): # n을 다 돌면서 앞뒤를 비교해야한다.
            if num + k > N or num - k < 1:
                break
            if arr[num+k] == arr[num-k]: # 인덱스에 k를 더한 값과 뺀 값이 같다면
                change(num+k)
                change(num-k)
            else:
                break

for i in range(1, N+1):
    print(arr[i], end= ' ')
    if i % 20 == 0:
        print()