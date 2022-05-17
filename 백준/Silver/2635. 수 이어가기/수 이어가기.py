n = int(input())

max_list = []

for i in range(1, n+1):
    list = [n]
    list.append(i)
    
    idx = 1
    
    while True:
        next_num = list[idx-1] - list[idx]
        
        if next_num < 0:
            break
        list.append(next_num)
        idx += 1
        
    if len(max_list) < len(list):
        max_list = list

print(len(max_list))
for i in max_list:
    print(i, end= ' ')