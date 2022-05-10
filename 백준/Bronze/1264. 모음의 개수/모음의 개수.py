while True:
    sum = 0
    a = input()
    if a == '#':
        break
    for i in a:
        if i in 'aeiouAEIOU':
            sum += 1
    
    print(sum)