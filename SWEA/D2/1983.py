T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    for i in range(N):
        a, b, c = map(int, input().split())
        sum = a * 0.35 + b * 0.45 + c * 0.2
        arr.append(sum)
    k_score = arr[K-1]
    arr.sort(reverse= True)
    
    tenrank = arr.index(k_score) // (N // 10) # arr에서 k_score가 몇 번째 등수인지 확인하고, 그걸 N / 10으로 나눠서 어떤 grade 확인
    k_grade = grade[tenrank]
    
    print('#{} {}'.format(tc, k_grade))