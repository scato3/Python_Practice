def solution(name, yearning, photo):
    result = []
    tmp = dict(zip(name, yearning))

    for i in photo:
        score = 0

        for k in i:
            score += tmp.get(k, 0)

        result.append(score)

    return result