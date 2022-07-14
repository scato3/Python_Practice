num = set(range(1, 10001))
tmp_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    tmp_num.add(i)

self_num = sorted(num - tmp_num)

for i in self_num:
    print(i)