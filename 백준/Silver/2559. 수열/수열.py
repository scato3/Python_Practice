n, k = map(int, input().split())
arr = list(map(int, input().split()))
sumarr = sum(arr[:k])
sumlist = [sumarr]

for i in range(len(arr) - k):
    sumarr = sumarr - arr[i] + arr[i+k]
    sumlist.append(sumarr)

print(max(sumlist))