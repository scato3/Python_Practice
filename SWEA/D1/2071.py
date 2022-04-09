T = int(input())
for test_case in range(1, T + 1):
    num = map(int, input().split())
    answer = 0
    result = 0;
    for i in num:
        answer += i
    result = round(answer/10)
    print("#" + str(test_case), str(result))