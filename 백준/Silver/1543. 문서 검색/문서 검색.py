a = input()
b = input()

start = 0
cnt = 0
for _ in range(len(a)):
    if a[start:start+len(b)] == b:
        cnt += 1
        start += len(b)
    else:
        start += 1

print(cnt)
