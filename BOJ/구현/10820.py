while True:
    try:
        text = list(input())
        lower, upper, n, blank = 0, 0, 0, 0
        for i in range(len(text)):
            if text[i] == ' ':
                blank += 1
            elif 65 <= ord(text[i]) <= 90:
                upper += 1
            elif 97 <= ord(text[i]) <= 122:
                lower += 1
            else:
                n += 1
        print(lower, upper, n, blank)
    except EOFError:
        break