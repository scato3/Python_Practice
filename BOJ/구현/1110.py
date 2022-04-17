# n = input() 시간 초과
# num = n
# cnt = 0
# while True:
#     if len(n) == 1:
#         num = num + '0'
#     plus = str(int(num[0]) + int(num[1]))
#     num = num[-1] + plus[-1]
#     cnt += 1
#     if num == n:
#         print(cnt)
#         break
     

n = int(input())
num = n
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    
    cnt += 1
    if num == n:
        print(cnt)
        break