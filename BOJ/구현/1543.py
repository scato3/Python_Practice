a = input()
b = input()

start = 0
cnt = 0

while start <= len(a) - len(b):
    if a[start:start+len(b)] == b:
        cnt += 1
        start += len(b)
    else:
        start += 1

print(cnt)