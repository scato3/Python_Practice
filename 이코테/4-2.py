h = int(input()) # 시간 입력 받기
count = 0

for i in range(h+1): # h+1을 한 이유는 N시 59분 59초까지 돌릴 것이기 때문에 h를 넣으면 5로 가정했을 때 4까지만 들어간다
    for j in range(60): # 분도 다 돌리고
        for k in range(60): # 초도 다 돌리고
            if '3' in str(i) + str(j) + str(k): # i, j, k에 대한 모든 값에서 3이 있으면 count
                count += 1
                
print(count)