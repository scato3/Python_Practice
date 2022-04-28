n = int(input())

arr = list(map(int, input().split())) # 손님이 원하는 값
box = set() # 중복을 허락하지 않는 박스를 만든다.
for i in arr:
    box.add(i) # 배열을 돌면서 중복을 제외하고 넣어준다.

print(len(arr) - len(box)) # 전체 값에서 중복을 뺀 값을 출력하면 거절 당한 사람의 수가 나온다.