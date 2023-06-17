def solution(players, callings):
    dic1 = {idx: i for i, idx in enumerate(players)}
    dic2 = {i: idx for i, idx in enumerate(players)}

    for x in callings:
        rank = dic1[x]

        dic1[dic2[rank-1]],dic1[dic2[rank]] = dic1[dic2[rank]], dic1[dic2[rank-1]]
        dic2[rank-1], dic2[rank] = dic2[rank], dic2[rank-1]

    return list(dic2.values())