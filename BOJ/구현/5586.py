a = input()
joi = 0
ioi = 0

for i in range(len(a) - 2):
    answer = ''
    answer += a[i] + a[i+1] + a[i+2]
    
    if answer == 'JOI':
        joi +=1
    if answer == 'IOI':
        ioi += 1
        
    

print(joi)
print(ioi)