n, m = map(int, input().split())
a = list(map(int, input().split()))
start = 0
end = 0
answer = 0

while start <= end and end <= len(a):
    summ = sum(a[start:end])
    if summ == m:
        answer += 1
    if summ <= m:
        end += 1
        continue
    elif summ > m and start < end:
        start += 1
        continue
    else:
        start += 1
        end += 1
print(answer)