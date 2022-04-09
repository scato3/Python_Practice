T = int(input())

for i in range(1, T+1):
    arr = input()
    pattern = ''
    for j in range(1, len(arr)+1):
        if arr[:j] == arr[j:j*2]: # j까지의 값과 j부터 2j까지의 값이 같으면 패턴이 같다는 뜻
            pattern = arr[:j]
            break
    print('#{} {}'.format(i, len(pattern)))