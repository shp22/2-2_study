def solution(players, m, k):
    tb = [0]*24
    for i, p in enumerate(players):
        temp = p // m
        cum = sum(tb[max(0,i-k+1):i+1])

        if temp > cum:
            tb[i] += temp - cum

    return sum(tb)