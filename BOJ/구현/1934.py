def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
    
def lcm(x, y):
    result = (x * y) // gcd(x, y)
    return result

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    print(lcm(x, y))
    
#유클리드 호제법으로 최대공약수 구하고 그것을 통해 최소공배수 구하기