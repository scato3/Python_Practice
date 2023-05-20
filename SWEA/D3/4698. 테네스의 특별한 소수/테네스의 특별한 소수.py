N = 10 ** 6
t = int(input())

def isPrime():
    for i in range(N+1):
        if prime[i] == 1:
            for j in range(i*2, N+1, i):
                prime[j] = 0


prime = [1] * (N+1)
prime[0], prime[1] = 0, 0
isPrime()

for tc in range(1, t+1):
    d, a, b = map(int, input().split())
    tmp = []

    for i in range(a, b+1):
        if str(d) in str(i) and prime[i]:
            tmp.append(i)
    print('#{} {}'.format(tc, len(tmp)))
