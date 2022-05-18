melon = int(input())

w, w_idx = 0, 0
h, h_idx = 0, 0

arr = [list(map(int, input().split())) for _ in range(6)]
    
for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if arr[i][1] > w :
            w = arr[i][1]
            w_idx = i
    elif arr[i][0] == 3 or arr[i][0] == 4:
        if arr[i][1] > h :
            h = arr[i][1]
            h_idx = i

subW = abs(arr[(w_idx - 1) % 6][1] - arr[(w_idx + 1) % 6][1])
subH = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1])

print((w * h - subW * subH) * melon)
