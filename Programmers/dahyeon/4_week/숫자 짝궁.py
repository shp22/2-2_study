def solution(X, Y):
    answer = []
    X, Y = list(X), list(Y)

    inter = set(X)&set(Y)
    print(inter)
    if inter == set():
        return '-1'
    elif inter == {'0'}:
        return '0'
    
    for c in inter:
        answer.append(c * min(X.count(c), Y.count(c)))

    answer.sort(key=lambda x: x[0], reverse=True)
    answer = ''.join(answer)
    return answer