arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))

num = list(map(int, input().split()))
for _ in range(4):
    num += list(map(int, input().split()))

check = [0] * 12
flag = False
ans = 0
for k in range(25):
    if flag:
        break
    for i in range(5):
        for j in range(5):
            if num[k] == arr[i][j]:
                arr[i][j] = 0
                check[i] += 1
                check[j+5] += 1
                if i == j:
                    check[10] += 1
                if i + j == 4:
                    check[11] += 1
                for l in range(12):
                    if check[l] == 5:
                        check[l] = 0
                        ans += 1
                    if ans == 3:
                        flag = True
                        break
print(k)
