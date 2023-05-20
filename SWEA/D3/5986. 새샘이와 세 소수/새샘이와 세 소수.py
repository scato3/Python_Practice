primes = []

for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.append(i)

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    m = len(primes)
    cnt = 0

    for i in range(m):
        if primes[i] > n:
            break
        for j in range(i, m):
            if primes[j] > n:
                break
            for k in range(j, m):
                if primes[k] > n:
                    break

                if primes[i] + primes[j] + primes[k] == n:
                    cnt += 1

    print('#{} {}'.format(tc, cnt))
