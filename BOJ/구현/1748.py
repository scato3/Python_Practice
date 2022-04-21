# n = int(input()) 시간초과 코드
# maxsum = ''

# if n < 10:
#     print(n)
    
# else:
#     for i in range(1, n+1):
#         maxsum += str(i)
#     print(len(maxsum)) 

n = int(input())

length = len(str(n))

cnt = 0

for i in range(length - 1):
    cnt += 9 * 10 ** i * (i+1)
    
