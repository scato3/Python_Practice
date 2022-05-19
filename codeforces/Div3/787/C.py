t = int(input())

for _ in range(t):
    n = input()
    cnt = 0

    for i in range(len(n)):
        if n[i] == '1':
            cnt = 1
        elif n[i] == '?':
            cnt += 1
        else:
            cnt += 1
            break

    print(cnt)