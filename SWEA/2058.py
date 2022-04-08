number = list(input()) # 각 자리 숫자가 list가 되도록 한다.
number = list(map(int, number)) # list(map())을 통해 문자열을 정수로 바꿔준다

sumNum = sum(number)
print(sumNum)