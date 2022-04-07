n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k # k의 개수
count += m % (k+1) # 안나눠졌을 때 추가해주는 k의 개수

result = 0
result += count * first
result += (m-count) * second

print(result)