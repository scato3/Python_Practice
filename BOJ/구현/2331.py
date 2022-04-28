a, b = map(int, input().split())
nums = [a] # 최초의 값 넣어준다.

while True:
    num = 0 # 자릿수의 b 제곱 값을 더할 변수를 지정
    for i in str(nums[-1]): # 마지막에 들어온 값을 처리하기 위해 str 처리
        num += int(i) ** b
    
    if num in nums:
        break
    else:
        nums.append(num) # 반복되지 않는다면 nums에 append 해준다.

print(nums.index(num))