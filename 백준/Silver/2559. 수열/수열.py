n, k = map(int, input().split())
arr = list(map(int, input().split()))

temp = sum(arr[:k])
lst = [temp]

for i in range(n-k):
    temp = temp - arr[i] + arr[i+k]
    lst.append(temp)

print(max(lst))