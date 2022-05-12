n = int(input())

for _ in range(n):
    arr = []
    students = list(map(int, input().split()))
    avg = (sum(students[1:]) / students[0])
    
    for i in students[1:]:
        if i > avg:
            arr.append(i)
    
    ans = (len(arr) / students[0]) * 100
    print(f'{ans:.3f}%')