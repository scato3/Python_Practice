n, k = map(int, input().split())
arr = list(map(int, input().split()))
sumarr = sum(arr[:k]) # ~ k 까지 다 더한다.
sumlist = [sumarr] # 최초의 값을 배열에 넣어준다.

for i in range(len(arr) - k): # + k까지 비교할 것이기 때문에 -k 까지 for문을 돌려줌
    sumarr = sumarr - arr[i] + arr[i+k] # 기존의 값에서 맨 앞의 arr값을 빼주고 k를 더해준 뒷 값을 더해주면 비교 가능!
    sumlist.append(sumarr)

print(max(sumlist))