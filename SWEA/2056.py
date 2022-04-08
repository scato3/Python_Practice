T = int(input())

for tc in range(1, T+1):
    date = input()
    month = int(date[4:6])
    day = int(date[6:])
    if month in (1, 3, 5, 7, 8, 10, 12):
        if day <= 31:
            print(f'#{tc} {date[:4]}/{date[4:6]}/{date[6:]}')
        else:
            print(f'#{tc} -1')
    elif month in (4, 6, 9, 11):
        if day <= 30:
            print(f'#{tc} {date[:4]}/{date[4:6]}/{date[6:]}')
        else:
            print(f'#{tc} -1')
    elif month == 2:
        if day <= 28:
            print(f'#{tc} {date[:4]}/{date[4:6]}/{date[6:]}')
        else:
            print(f'#{tc} -1')
    else:
      print(f'#{tc} -1')  
