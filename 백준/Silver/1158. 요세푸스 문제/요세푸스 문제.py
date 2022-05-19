a, b = map(int, input().split())
arr = [i for i in range(1, a+1)]

num = b - 1
answer = []
for i in range(a):
    if len(arr) > num:
        answer.append(arr.pop(num))
        num += b - 1
    elif len(arr) <= num:
        num = num % len(arr)
        answer.append(arr.pop(num))
        num += b - 1
        
print('<', ', '.join(str(i) for i in answer), '>', sep= '')
    