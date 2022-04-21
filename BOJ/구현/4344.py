n = int(input())
avg = 0

for _ in range(n):
    students = list(map(int, input().split()))
    avg = sum(students[1:]) / students[0]
    cnt = 0
    for score in students[1:]:
        if score > avg:
            cnt += 1
    ans = (cnt / students[0]) * 100
    print(f'{ans:.3f}%')