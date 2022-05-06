n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(str, input())))
    
cnt = 0
res = ''


for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    
    for j in range(n):
        if arr[j][i] == 'A':
            a += 1
        elif arr[j][i] == 'C':
            c += 1
        elif arr[j][i] == 'G':
            g += 1
        elif arr[j][i] == 'T':
            t += 1
    if max(a, c, g, t) == a:
        res += 'A'
        cnt += c + g + t
    elif max(a, c, g, t) == c:
        res += 'C'
        cnt += a + g + t
    elif max(a, c, g, t) == g:
        res += 'G'
        cnt += a + c + t
    elif max(a, c, g, t) == t:
        res += 'T'
        cnt += a + c + g

print(res)
print(cnt)
