n = int(input())
nums = list(map(int, input().split()))
cnt = 0
def isPrime(n):
    if n <= 1:
        return 0
    else:
        for i in range(2, n):
            if n % i == 0:
                return 0
        else:
            return 1

for i in range(n):
    cnt += isPrime(nums[i])
print(cnt)
